import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.table as tbl
import seaborn as sns
import pandas as pd
import numpy as np
import os, json

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Patch
from os import system
from pathlib import Path

clear = lambda: system('cls')
plt.rcParams.update({'figure.max_open_warning': 0})

############################## helper functions ####################################
def fix_report_dataframe(df, sort_by, decimals, ascend=False, place=1):
    '''places 'sort by' at the front, sorts, and rearranges columns for intent_report.json
        df      : pandas DataFrame created from intent_report
        sort_by : 'precision', 'recall', 'f1-score', or 'samples'
        decimals: number of places to round to
        place   : index location for sort_by in table, default to intents being first
        ascend  : if the returned DF should sort by ascending sort_by values
        returns : pandas DataFrame '''

    # make 'intents' a column instead of index and rename
    df.reset_index(level=0, inplace=True)
    df = df.rename(columns={'support':'samples', 'index':'intent'})

    # round floating values
    df['precision'] = df['precision'].apply(lambda x: np.round(x, decimals))
    df['recall'] = df['recall'].apply(lambda x: np.round(x, decimals))
    df['f1-score'] = df['f1-score'].apply(lambda x: np.round(x, decimals))
    df['confused_with'] = df['confused_with'].apply(lambda x: str(x).strip("{/}"))

    # re-organize columns with the 'sort_by' first
    new_cols = list(df.columns)
    new_cols.remove(sort_by)
    new_cols.insert(place, sort_by)
    df = df[new_cols]

    # remove 'button' intents and move averages to bottom of list
    df = df[~df.intent.str.contains("button")]
    df_temp = df[df.intent.str.contains("avg")]
    df = df[~df.intent.str.contains("avg")]
    
    # sort and return with averages at end
    df.sort_values(by=[sort_by], ascending=ascend, inplace=True)
    return df.append(df_temp)

def track_fig(fig, f_d, num):
    '''adds a plt figure to tracking dict for saving to PDF
        fig     : the current plt.gcf() to save
        f_d     : the tracking dictionary for figs
        num     : how many figs were added before the current one
        returns : updated dict and fig tracking number'''
    f_d[num] = fig
    return f_d, num+1

def get_report_df(p_d, r, i_r):
    '''generates DataFrame from report json
        p_d     : path dictionary for reports
        r       : report prefix / key value
        i_r     : intent report json filename
        returns : unformatted DataFrame'''

    os.chdir(p_d[r])
    with open(i_r) as f:
        data = json.load(f)
    
    # remove 'accuracy' since it's the same as 'recall' for weighted_avg
    data.pop('accuracy', None)

    return pd.DataFrame.from_dict(data, orient='index')

def get_errors_df(p_d, r, e_r):
    '''generates DataFrame from intent errors report
    p_d     : path dictionary for reports
    r       : report prefix / key value
    e_r     : error report json filename
    returns : formatted DataFrame'''

    os.chdir(p_d[r])
    df = pd.read_json(intent_errors, orient='records')
    df['confidence'] = df['intent_prediction'].apply(lambda x: x['confidence'])
    df['intent_prediction'] = df['intent_prediction'].apply(lambda x: x['name'])
    df['confidence'] = df['confidence'].apply(lambda x: np.round(x, decimals))
    df = df.groupby(['intent']).apply(pd.DataFrame.sort_values, 'confidence', ascending=False)[['text', 'intent_prediction', 'confidence']]
    
    return df.reset_index()[['text', 'intent', 'intent_prediction', 'confidence']]

def get_err_con_sum_df(target, df):
    '''make error-confidence summary DataFrames for target column
        target  : string name of column to get average confidences for
        df      : DataFrame with confidence and target columns
        returns : DataFrame with averaged confidence for grouped target column content
    '''
    df_trim = df[[target, 'confidence']]
    df_grouped = df_trim.groupby([target]).mean()
    df_grouped.reset_index(inplace=True)
    counts = dict(df_trim[target].value_counts())
    df_grouped['count'] = df_grouped[target].apply(lambda x: counts[x])
    df_grouped.sort_values(by=['confidence'], ascending=False, inplace=True)
    df_grouped['confidence'] = df_grouped['confidence'].apply(lambda x: np.round(x, decimals))

    return df_grouped

##########################################################################################################################


# directory path where reports are saved
data_dir = os.getcwd()

# directory names within data_dir for reports to compare
correct = '0'
while not int(correct):
    report_dirs = []
    clear()
    print("\nPlease enter the directory names (eg: '1pm' - without the quotes) for each directory.\n")
    dir_name = ""
    for i in range(1,3):
        output = "Name of report directory " + str(i) + ": "
        dir_name = input(output)
        print('')
        report_dirs.append(dir_name)

    clear()
    # respective prefixes to be appended for report output
    reports = []
    print("\nPlease enter the report names (eg: 'Report 1' - without the quotes) you would like\n \
    to label each report with.\n")
    report_name = ""
    for i in range(2):
        output = "Name for output from " + report_dirs[i] + ": "
        report_name = input(output)
        print('')
        reports.append(report_name)

    clear()
    print("\nYour rasa report directories are: ", report_dirs)
    print("Your output report directories will be: ", reports)
    print("Are these correct?\n")
    correct = input("Enter '0' for 'No', or any other number for 'Yes': ")
clear()
print("\nCreating report summaries now...\n")

# directory name for generated output - will be placed in data_dir
output_dir = "report_summaries"

# report filenames (if saved as something else)
# these must be the same for all reports and structured as the rasa-generated files
intent_report = "intent_report.json" # 'ir'
intent_errors = "intent_errors.json" # 'ie'

# preferences for cleaning up data into tables
sort_by = 'f1-score'    # ['precision', 'recall', 'f1-score', 'samples']
decimals = 3            # number of decimal places to round values to
rows_pp = 27            # number of rows per page for tables, to avoid smooshing
threshold = 3           # minimum number of pairings to be included in output

# navigate to data_dir
os.chdir(data_dir)

# for tracking generated images and saving to pdf
fig_dicts, fig_trackers, path_dict, error_dicts, error_trackers = {}, {}, {}, {}, {}

for i in range(len(reports)):
    fig_dicts[reports[i]] = {}
    fig_trackers[reports[i]] = 0
    path_dict[reports[i]] = os.path.join(data_dir, report_dirs[i])
    error_dicts[reports[i]] = {}
    error_trackers[reports[i]] = 0

# for comparisons
combined_figs = {}
combined_tracker = 0

## INTENT REPORT SUMMARY TABLES
#### sorted by 'sort_by', builds a table with a row summarizing model performance for each intent.
#### "Samples" represents the number of NLU training samples available to the model for that intent.
#### "confused_with" lists other intents mistakenly predicted instead of the correct (current) inent.

for r in reports:
    # create DataFrame for intent reports
    summary_df = get_report_df(path_dict, r, intent_report)
    summary_df = fix_report_dataframe(summary_df, sort_by, decimals)
    # variables for formatting
    font_size = 11
    num_cols = len(summary_df.columns)
    num_rows = len(summary_df)
    rec_ind = summary_df.columns.get_loc("recall")
    num_pages = num_rows//rows_pp
    if num_rows % rows_pp > 0:
        num_pages += 1

    for i in range(num_pages):
        # partial DataFrame to fit to page
        temp_df = summary_df.iloc[i*rows_pp:(i+1)*rows_pp]
        num_rows = len(temp_df)
        last_page = i==(num_pages-1)

        # create summary table
        fig, ax = plt.subplots(figsize=(8.5,11), dpi=150)
        ax.axis('off')
        ax.axis('tight')
        the_table = ax.table(cellText=temp_df.values,
                            colLabels=temp_df.columns, 
                            loc='center', 
                            colColours=["gold"] * num_cols, 
                            colWidths=[.2,.1,.1,.1,.1,.4])

        # fix formatting
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(font_size)

        # cell highlighting
        for j in range(num_cols):
            the_table[0,j].set_text_props(weight="bold")
            if last_page:
                the_table[num_rows,j].set_facecolor("gainsboro")
                the_table[num_rows-1,j].set_facecolor("gainsboro")
        
        # 'accuracy' cell callout
        if last_page:
            accuracy_cell = the_table[num_rows, rec_ind]
            accuracy_cell.set_text_props(style="italic")
            accuracy_cell.set_facecolor("lightcoral")
            accuracy_cell.set_linewidth(2)

        # row and text spacing
        cells = the_table.get_celld()
        for j in range(1, num_rows+1):
            cells[j, 5].PAD = 0.01
            cells[j, 0].PAD = 0.02

            # newlines for confused intents
            cell_text = cells[j, 5].get_text().get_text()
            extra_height = cell_text.count(',')
            if extra_height:
                cell_text = cell_text.replace(',', '\n')
                text_size = font_size - (0.5 * extra_height)
                cells[j, 5].get_text().set_text(cell_text)
                cells[j, 5].get_text().set_size(text_size)
                for k in range(num_cols):
                    cells[j,k]._height += (0.015 * extra_height)

        # label and save
        fig.tight_layout()
        title = r + " Intent Accuracy Summary"
        subtitle = "Table " + str(i+1) + " of " + str(num_pages)
        plt.title(title, y=0.98, fontdict={'fontsize':16, 'fontweight':"bold", 'horizontalalignment': "center"})
        plt.figtext(x=0.5, y=0.96, s=subtitle, ha="center")
        if last_page:
            ax.legend(handles=[Patch(facecolor='lightcoral', edgecolor='black', label='Overall Accuracy')], loc='lower center')
        fig_dicts[r], fig_trackers[r] = track_fig(plt.gcf(), fig_dicts[r], fig_trackers[r])
        #plt.clf()

print("Finished summary tables, starting performance ranking...\n")
# INTENT F1 RANKINGS
for r in reports:
    # create DataFrame for intent reports
    summary_df = get_report_df(path_dict, r, intent_report)
    summary_df = fix_report_dataframe(summary_df, sort_by, decimals)
    summary_df = summary_df[~summary_df.intent.str.contains("avg")] # remove averages from scatterplots

    # Make the PairGrid
    g = sns.PairGrid(summary_df,
                    x_vars=summary_df.columns[1:-2], y_vars=["intent"],
                    height=10, aspect=.25)

    # Draw a dot plot using the stripplot function
    g.map(sns.stripplot, size=10, orient="h", jitter=False,
        palette="plasma", linewidth=1, edgecolor="w")

    # Use the same x axis limits on all columns and add better labels
    g.set(xlim=(0, 1), xlabel="Percentage", ylabel="")

    # titles for selected columns from DataFrame
    titles = ["F1-Score", "Precision", "Recall"]

    for ax, title in zip(g.axes.flat, titles):

        # Set a different title for each axes
        ax.set(title=title)

        # Make the grid horizontal instead of vertical
        ax.xaxis.grid(False)
        ax.yaxis.grid(True)

    sns.despine(left=True, bottom=True)
    title = r + " Intent f1 Ranking"
    g.fig.subplots_adjust(top=0.935) # adjust the Figure to make space for title
    g.fig.suptitle(title, x=0.45, size=16, weight='bold')
    fig_dicts[r], fig_trackers[r] = track_fig(plt.gcf(), fig_dicts[r], fig_trackers[r])
    #plt.clf()

## combine intent reports for comparisons
column_names = ["report", "intent", "precision", "recall", "f1-score", "samples", "confused_with"]
combined_df = pd.DataFrame(columns=column_names)

# slightly modified fix_report_dataframe()
for r in reports:
    temp_df = get_report_df(path_dict, r, intent_report)
    temp_df = fix_report_dataframe(temp_df, 'intent', decimals, True, 0) # sort by intent
    temp_df["report"] = r # new column with report name
    combined_df = combined_df.append(temp_df)

combined_df = combined_df[~combined_df.intent.str.contains("avg")] # remove averages from reports

print("Finished performance ranking, creating performance shift diagrams...\n")
## Intent Performance Shifts
intents = combined_df.intent.unique()
colors = ["DarkSeaGreen", "BurlyWood", "Crimson"]
for z in range(2):
    sns.set_style("darkgrid")
    with sns.plotting_context(rc={"legend.title_fontsize":12, "legend.fontsize":10, "axes.labelsize":14,"plt.subplots.figsize":(8.5,11)}):

        sns.relplot(x="precision", y="recall", 
                    hue="report", palette="Blues", 
                    size="samples", sizes=(50, 450), 
                    data=combined_df, height=16, aspect=0.8,
                    )
        fig.tight_layout()
        title = "Intent Performance Shifts"
        plt.title(title, fontdict={'fontsize':16, 'fontweight':"bold", 'horizontalalignment': "center"})

        for intent in intents:
            temp_df = combined_df.loc[combined_df['intent'] == intent]
            temp_df = temp_df[['intent', 'recall', 'precision']]
            x = temp_df['precision'].to_list()
            y = temp_df['recall'].to_list()
            color = 0
            width = 0
            if len(x) > 1:
                if x[0] > x[1]:
                    color += 1
                if y[0] > y[1]:
                    color += 1
                width = (abs(x[0]-x[1]) + abs(y[0]-y[1])) * 8  
            temp_df['color'] = color
                
            for i in range(len(y)-1):
                sns.lineplot(x='precision', y='recall', data=temp_df, linewidth=width, color=colors[color], legend=False)

            # place text and lines
            if z:
                plt.text(x[0]+0.0065,y[0]-0.0015,intent, horizontalalignment='left', wrap=True)

    combined_figs, combined_tracker = track_fig(plt.gcf(), combined_figs, combined_tracker)
    #plt.clf()

## INTENT ACCURACY MEAN COMPARISON
combined_df_trim = combined_df[["report", "precision", "recall", "f1-score"]]
combined_df_trim = pd.melt(combined_df_trim, "report", var_name="measurement")
# Initialize the figure
fig, ax = plt.subplots(figsize=(11,8.5))
sns.despine(bottom=True, left=True)

# Show each observation with a scatterplot
sns.stripplot(x="value", y="measurement", hue="report",
              data=combined_df_trim, dodge=True, alpha=0.5, zorder=1, jitter=0.1, size=6)

# Show the conditional means
sns.pointplot(x="value", y="measurement", hue="report",
              data=combined_df_trim, dodge=0.4, join=False, palette="dark",
              markers="d", scale=1.3, ci=None)

# Improve the legend 
handles, labels = ax.get_legend_handles_labels()
ax.get_legend().remove()
fig.legend(handles[2:], labels[2:],
          handletextpad=0, columnspacing=1,
          loc="lower center", ncol=2, frameon=True)

fig.subplots_adjust(top=0.935) # adjust the Figure to make space for title
fig.suptitle("Intent Accuracy Mean Comparison", size=16, weight='bold')
combined_figs, combined_tracker = track_fig(plt.gcf(), combined_figs, combined_tracker)
#plt.clf()

### INTENT CONFUSION IMPROVEMENT MATRIX
# errors from Reprt 1 for heatmap
errors_df = get_errors_df(path_dict, reports[0], intent_errors)
errors_df = errors_df.groupby(['intent', 'intent_prediction']).size()
errors_df = errors_df.reset_index()
errors_df.rename(columns={'intent':'intended', 'intent_prediction':'predicted'}, inplace=True)

# all unique intents from both reports for heatmap
intents = combined_df.intent.unique().tolist()
intents.sort()
intended = []
predicted = []
for intent in intents:
    intended.extend([intent] * len(intents))
    predicted.extend(intents)

# add number of times intents were mistaken
pairs = []
for i in range(len(intended)):
    val = 0
    results = errors_df.loc[(errors_df['intended'] == intended[i]) & (errors_df['predicted'] == predicted[i])]
    if len(results):
        val = int(results.iloc[0,2])
    pairs.append(val)

# dataframe for confusion matrix / heatmap
matrix_df = pd.DataFrame(list(zip(intended, predicted, pairs)), columns=['intended', 'predicted', 'paired'])

# create new maps for each other report and calculate difference from first report
for r in range(1,len(reports)):
    errors_df = get_errors_df(path_dict, reports[r], intent_errors)
    errors_df = errors_df.groupby(['intent', 'intent_prediction']).size()
    errors_df = errors_df.reset_index()
    errors_df.rename(columns={'intent':'intended', 'intent_prediction':'predicted'}, inplace=True)
    pairs = []
    for i in range(len(intended)):
        val = 0
        results = errors_df.loc[(errors_df['intended'] == intended[i]) & (errors_df['predicted'] == predicted[i])]
        if len(results):
            val = int(results.iloc[0,2])
        pairs.append(val)
    matrix_df['paired'] = matrix_df['paired'] - pairs

# create offset to make '0' center of color range
offset = mcolors.TwoSlopeNorm(vmin=matrix_df['paired'].min(),
                            vcenter=0, vmax=matrix_df['paired'].max())
normal_change = list(offset(matrix_df['paired'].tolist()))
annotation_vals = matrix_df['paired'].tolist()

# fix annotation list shape for frame
jump = len(intents)
annotations = []
for i in range(jump):
    annotations.append(annotation_vals[i*jump:(i+1)*jump])
annotations = np.array(annotations)

# pivot table for confusion matrix layout
matrix_df['paired'] = normal_change
matrix_df = matrix_df.pivot("intended", "predicted", "paired")

# Draw a heatmap with the numeric values in each cell from annotations
fig, ax = plt.subplots(figsize=(15, 15))
sns.heatmap(matrix_df, annot=annotations, fmt="d", linewidths=.5, ax=ax, cmap='PiYG',
                 cbar=False)
                 #cbar_kws={"orientation": "horizontal", "pad":0.12}
fig.subplots_adjust(top=0.955) # adjust the Figure to make space for title
fig.suptitle("Intent Confusion Improvement Matrix", size=16, weight='bold')
combined_figs, combined_tracker = track_fig(plt.gcf(), combined_figs, combined_tracker)
#plt.clf()

print("Completed perfromance comparison diagrams, beginning individual reports...")
print("(this could take some time)\n")
### SCATTERPLOT DIAGRAMS FOR INDIVIDUAL REPORTS
for r in reports:
    # structure DataFrame for diagram plotting
    scatter_df = get_report_df(path_dict, r, intent_report)
    scatter_df = fix_report_dataframe(scatter_df, sort_by, decimals)
    scatter_df = scatter_df[~scatter_df.intent.str.contains("avg")] # remove averages from scatterplots

    # one plot with intent label text, one without
    for i in range(2):
        sns.set_style("darkgrid")
        with sns.plotting_context(rc={"legend.title_fontsize":12, "legend.fontsize":10, "axes.labelsize":14,"plt.subplots.figsize":(8.5,11)}):
            plot = sns.relplot(x="precision", y="recall", 
                        hue="f1-score", palette="ch:r=-.5,l=.75", 
                        size="samples", sizes=(15, 450), 
                        data=scatter_df, height=10, aspect=0.8,
                        )
            fig.tight_layout()
            title = r + " Intents Scattergram"
            plt.title(title, fontdict={'fontsize':16, 'fontweight':"bold", 'horizontalalignment': "center"})

            # place text on second iteration
            if i:
                for idx,row in scatter_df.iterrows():
                    x = row[2]
                    y = row[3]
                    text = row[0]
                    plt.text(x+0.0065,y-0.0015,text, horizontalalignment='left', wrap=True)
            # save figs for PDF
            fig_dicts[r], fig_trackers[r] = track_fig(plt.gcf(), fig_dicts[r], fig_trackers[r])
            #plt.clf()

## Generate tables for intent errors
for r in reports:
    # DataFrame and variables for formatting
    errors_df = get_errors_df(path_dict, r, intent_errors)
    font_size = 10
    num_cols = len(errors_df.columns)
    num_rows = len(errors_df)
    num_pages = num_rows//rows_pp
    if num_rows % rows_pp > 0: num_pages += 1

    # break all intent errors into multiple tables
    for i in range(num_pages):
        # temporary DataFrame to iterate through all intent errors
        temp_df = errors_df.iloc[i*rows_pp:(i+1)*rows_pp]
        fig, ax = plt.subplots(figsize=(8.5,11), dpi=150)
        ax.axis('off')
        ax.axis('tight')
        the_table = tbl.table(ax,
                            cellText=temp_df.values, 
                            colLabels=temp_df.columns, 
                            loc='center', 
                            colColours=["gold"] * num_cols,
                            colWidths=[.52,.18,.18,.12],
                            )
        # formatting 
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(font_size)
        the_table.scale(1,1.1)
        for j in range(num_cols):
            the_table[0,j].set_text_props(weight="bold")

        
        cells = the_table.get_celld()
        for j in range(1, len(temp_df)+1):
            cells[j, 0].PAD = 0.01
            cells[j, 1].PAD = 0.015
            cells[j, 2].PAD = 0.015

            # edit long text and apply changes
            cell_text = cells[j, 0].get_text().get_text().replace('$$','\\$\\$')
            cut = 60
            text_size = font_size
            while len(cell_text) > cut:
                for k in range(num_cols):
                    cells[j,k]._height += 0.015
                insert_at = cell_text[:cut].rfind(' ')
                cell_text = cell_text[:insert_at] + '\n' + cell_text[insert_at:]
                text_size -= 0.15
                cut += 60  
            cells[j, 0].get_text().set_text(cell_text)
            cells[j, 0].get_text().set_size(text_size)

            # edit 'button' intent text and apply
            for k in range(1,3):
                cell_text = cells[j, k].get_text().get_text()
                if len(cell_text) > 18:
                    cells[j, k].get_text().set_size(font_size-1.5)

            # highlight every other row
            if j%2 == 0:
                for k in range(num_cols):
                    cells[j,k].set_facecolor("gainsboro")

        # label and save tables
        fig.tight_layout()            
        title = r + " Intent Errors"
        subtitle = "Table " + str(i+1) + " of " + str(num_pages)
        plt.title(title, fontdict={'fontsize':16, 'fontweight':"bold"})
        plt.figtext(x=0.5, y=0.95, s=subtitle, ha="center")
        plt.tight_layout()
        error_dicts[r], error_trackers[r] = track_fig(plt.gcf(), error_dicts[r], error_trackers[r])
        #plt.clf()

# Confidence Averages for Errors
for r in reports:
    errors_df = get_errors_df(path_dict, r, intent_errors)
    intent_con_df = get_err_con_sum_df('intent', errors_df)
    predict_con_df = get_err_con_sum_df('intent_prediction', errors_df)

    num_cols = len(intent_con_df.columns)

    # create figure for 2 tables
    fig, axes = plt.subplots(ncols=2, figsize=(8.5, 11))
    table_1 = plt.subplot(1, 2, 1)
    table_2 = plt.subplot(1, 2, 2)

    # intents table
    table_1.axis('off')
    table_1.axis('tight')
    the_table = table_1.table(cellText=intent_con_df.values, 
                        colLabels=intent_con_df.columns, 
                        loc='center', 
                        colColours=["gold"] * num_cols, 
                        rowLoc='center',
                        colWidths=[.6,.23,.17])
    
    # formatting
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(11)
    for j in range(num_cols):
        the_table[0,j].set_text_props(weight="bold")
    cells = the_table.get_celld()
    for j in range(1, len(intent_con_df)+1):
        if j%2 == 0:
            for k in range(num_cols):
                cells[j,k].set_facecolor("gainsboro")

    # intent_predictions table
    table_2.axis('off')
    table_2.axis('tight')
    the_table = table_2.table(cellText=predict_con_df.values, 
                        colLabels=predict_con_df.columns, 
                        loc='center', 
                        colColours=["gold"] * num_cols, 
                        rowLoc='center',
                        colWidths=[.6,.23,.17])
    
    # formatting
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(11)
    for j in range(num_cols):
        the_table[0,j].set_text_props(weight="bold")
    cells = the_table.get_celld()
    for j in range(1, len(predict_con_df)+1):
        if j%2 == 0:
            for k in range(num_cols):
                cells[j,k].set_facecolor("gainsboro")


    # legends
    height_adjust   = 0.021
    t1_pos = 0.5 - (len(intent_con_df)/2 * height_adjust)
    t2_pos = 0.5 - (len(predict_con_df)/2 * height_adjust)
    fig.tight_layout()
    title = r + " Confidence Averages for Errors"
    plt.title(title, x=0, y=0.96, fontdict={'fontsize':16, 'fontweight':"bold", 'horizontalalignment': "center"})
    t1_sub1 = "'count' = Number of times the intent was missed"
    t2_sub1 = "'count' = Number of times the intent was incorrectly used"
    t1_sub2 = "'confidence' = Avg confidence when intent was missed"
    t2_sub2 = "'confidence' = Avg confidence when intent was incorrectly used"
    plt.figtext(x=0.25, y=t1_pos, s=t1_sub1, ha="center", fontsize=10)
    plt.figtext(x=0.75, y=t2_pos, s=t2_sub1, ha="center", fontsize=10)
    plt.figtext(x=0.25, y=t1_pos-.015, s=t1_sub2, ha="center", fontsize=10)
    plt.figtext(x=0.75, y=t2_pos-.015, s=t2_sub2, ha="center", fontsize=10)

    # track tables for pdf
    fig_dicts[r], fig_trackers[r] = track_fig(plt.gcf(), fig_dicts[r], fig_trackers[r])
    #plt.clf()

# column_names = ["report", "intent", "confidence", "count"]
# combo_err_df = pd.DataFrame(columns=column_names)
# # Intent Error Pairing Counts
# column_names = ["report", "intent", "intent_prediction", "count"]
# combined_pairings_df = pd.DataFrame(columns=column_names)

# # slightly modified fix_report_dataframe()
# for r in reports:
#     temp_err_df = get_errors_df(path_dict, r, intent_errors)
#     temp_int_df = get_err_con_sum_df('intent', temp_err_df)
#     temp_pred_df = get_err_con_sum_df('intent_prediction', temp_err_df)

#     # new cols for reports
#     temp_int_df["report"] = r
#     temp_pred_df["report"] = r

#     combo_err_df = combo_err_df.append(temp_int_df)
#     combo_pred_err_df = combo_pred_err_df.append(temp_pred_df)

column_names = ["report", "intent", "intent_prediction", "count"]
combined_pairings_df = pd.DataFrame(columns=column_names)

for r in reports:
    errors_df = get_errors_df(path_dict, r, intent_errors)
    count_pairings = errors_df.groupby(['intent', 'intent_prediction']).size()
    pairing_counts = count_pairings.to_frame(name='count').reset_index()
    pairing_counts.sort_values(by=['count'], ascending=False, inplace=True)
    count_series = errors_df.groupby(['intent', 'intent_prediction']).mean()
    count_series.reset_index(inplace=True)
    joined_df = pairing_counts.merge(count_series, on=["intent", "intent_prediction"])
    joined_df['confidence'] = joined_df['confidence'].apply(lambda x: np.round(x, decimals))
    joined_df = joined_df[joined_df['count'] >= threshold]

    # combined pairings DF
    temp_df = joined_df[joined_df['count'] >= threshold]
    temp_df["report"] = r
    combined_pairings_df = combined_pairings_df.append(temp_df)

    font_size = 11
    rows_per_page = 40
    num_cols = len(joined_df.columns)
    num_rows = len(joined_df)
    num_pages = num_rows//rows_per_page
    if num_rows % rows_per_page > 0: num_pages += 1

    for i in range(num_pages):
        temp_df = joined_df.iloc[i*rows_per_page:(i+1)*rows_per_page]
        fig, ax = plt.subplots(figsize=(8.5,11), dpi=150)
        ax.axis('off')
        ax.axis('tight')
        the_table = ax.table(cellText=temp_df.values, 
                            colLabels=temp_df.columns, 
                            loc='center', 
                            colColours=["gold"] * len(temp_df.columns), 
                            colWidths=[.35,.35,.1,.2])

        # formatting
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(11)
        for j in range(num_cols):
            the_table[0,j].set_text_props(weight="bold")
        cells = the_table.get_celld()
        for j in range(1, len(temp_df)+1):
            if j%2 == 0:
                for k in range(num_cols):
                    cells[j,k].set_facecolor("gainsboro")

        fig.tight_layout()
        title = r + " Intent Pairings"
        subtitle = "Table " + str(i+1) + " of " + str(num_pages)
        table_text = "                    Intent pairings below the threshold of " + str(threshold) + " occurences have not been included\n\
                    'count' = number of times the prediction was mistakenly used instead of the correct intent\n\
                    'confidence' = average confidence all all mistaken predictions"
        plt.title(title, fontdict={'fontsize':16, 'fontweight':"bold"})
        plt.figtext(x=0.5, y=0.955, s=subtitle, ha="center")
        if not i:
            plt.figtext(x=0.5, y=0.905, s=table_text, ha="center")
        plt.tight_layout()
        fig_dicts[r], fig_trackers[r] = track_fig(plt.gcf(), fig_dicts[r], fig_trackers[r])
        #plt.clf()

### EXPORT TO PDFS
print("Completed individual report summaries, exporting to PDFs...")
print("(this may also takes some time)\n")

# create output dir and save reports to it
output_path = os.path.join(data_dir, output_dir)
Path(output_path).mkdir(mode=0o777, parents=False, exist_ok=True)

for r in reports:
    os.chdir(output_path)
    report_dir = os.path.join(output_path, r)
    Path(report_dir).mkdir(mode=0o777, parents=False, exist_ok=True)
    os.chdir(report_dir)
    
    # report figs
    pdf_name = r + " figs.pdf"
    with PdfPages(pdf_name) as pdf:
        for key in fig_dicts[r]:
            pdf.savefig(fig_dicts[r][key], bbox_inches='tight')

    # error tables
    pdf_name = r + " errors.pdf"
    with PdfPages(pdf_name) as pdf:
        for key in error_dicts[r]:
            pdf.savefig(error_dicts[r][key], bbox_inches='tight')

# comparison figs
os.chdir(output_path)
pdf_name = "Report Comparisons.pdf"
with PdfPages(pdf_name) as pdf:
    for key in combined_figs:
        pdf.savefig(combined_figs[key], bbox_inches='tight')

print("Completed report summaries and comparison!")
print("Output can be found in the new 'report_summaries' folder")
