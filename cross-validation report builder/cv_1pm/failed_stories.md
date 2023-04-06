## Auto Pay Setup = False and Past Due Balance = False, View my bill and Transfer to expert (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I would like to pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_not_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_not_exists"}
    - utter_ca_bp_001_2   <!-- predicted: utter_broken -->
* button_link_view_my_bill: /button_link_view_my_bill
    - action_delay_5_minutes   <!-- predicted: action_delay_45_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* transfer_to_expert: expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## Auto Pay Setup = False and Past Due Balance = True and PA Eligible Created (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I need to pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_not_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_exists"}
    - utter_ca_bp_001_3   <!-- predicted: utter_ca_bp_001_20 -->
* pa_create: Payment Arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "secured"}
    - utter_pa_new_setup   <!-- predicted: utter_fallback_first -->
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## pa eligible survey (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "secured"}
    - utter_pa_new_setup   <!-- predicted: utter_fallback_first -->
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## pa eligible wait (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up  payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat


## pa eligible wait 2 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up  payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat


## pa eligible wait 2 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat


## pa eligible survey (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "secured"}
    - utter_pa_new_setup   <!-- predicted: utter_fallback_first -->
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, Thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## pa eligible survey 2 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up  payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "secured"}
    - utter_pa_new_setup   <!-- predicted: utter_fallback_first -->
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, Thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## pa eligible transfer expert (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up  payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "secured"}
    - utter_pa_new_setup   <!-- predicted: utter_fallback_first -->
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* transfer_to_expert: Chat with a live Expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## pa eligible transfer main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "secured"}
    - utter_pa_new_setup   <!-- predicted: utter_fallback_first -->
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* bill_general: Billing
    - utter_ca_ot_008_jump_billing   <!-- predicted: utter_ca_ot_004_menu_plan -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Auto Pay Setup = True and Account Balance = $0 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I would like to pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "account_balance_zero"}
    - utter_ca_bp_bill0_01   <!-- predicted: utter_ca_bp_001_32 -->


## pa eligible help (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
* button_need_help: I need help
    - utter_ca_aem_help_001   <!-- predicted: utter_pa_unsecured_choices -->
* transfer_to_expert: chat with expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## pa ineligible why yes (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* why: why
    - utter_ineligible_expert   <!-- predicted: utter_ca_ot_020_jump_order_status -->
* affirm: yes
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## pa ineligible why deny (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* why: why
    - utter_ineligible_expert   <!-- predicted: utter_ca_ot_020_jump_order_status -->
* deny: no
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## pa ineligible why deny 2 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* why: why
    - utter_ineligible_expert   <!-- predicted: utter_ca_ot_020_jump_order_status -->
* deny: no, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## pa ineligible bill (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* bill_general: bill
    - utter_ca_ot_008_jump_billing   <!-- predicted: utter_ca_ot_004_menu_plan -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## pa eligible main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


## pa eligible main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: set up payment arrangement
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* broken: Link is broken
    - utter_broken   <!-- predicted: utter_transfer_expert -->
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## pa not secured add help test (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "not_secured"}
    - utter_pa_unsecured_choices   <!-- predicted: utter_pa_addpay_link -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start


## Auto Pay Setup = True and Account Balance = Negative (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I would like to pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "account_balance_negative"}
    - utter_ca_bp_apcredit_01   <!-- predicted: utter_ca_bp_001_5 -->


## pa not secured add help test (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "not_secured"}
    - utter_pa_unsecured_choices   <!-- predicted: utter_pa_addpay_link -->
    - action_delay_2_minutes
* speak_spanish: I speak spanish
    - utter_transfer_spanish   <!-- predicted: utter_welcome -->


## Story from conversation with 6942789b-761f-4095-86e6-35da42c9a484 on September 11th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-ab10d244-844c-4d29-bb33-ec41a4da6176"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "8135100988"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "959335288"}
    - slot{"first_name": "Jamille"}
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - slot{"pa_link": "https://t-mo.cc/mwfxv1lf9e"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
    - slot{"repeat_end_time": "2020-09-11T15:49:38.164565"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:55:40.104499"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:55:40.104499"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* button_need_help: I need help
    - utter_ca_aem_help_001   <!-- predicted: utter_pa_unsecured_choices -->


## Story from conversation with 6942789b-761f-4095-86e6-35da42c9a484 on September 11th 2020ssss (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-ab10d244-844c-4d29-bb33-ec41a4da6176"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "8135100988"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "959335288"}
    - slot{"first_name": "Jamille"}
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - slot{"pa_link": "https://t-mo.cc/mwfxv1lf9e"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
    - slot{"repeat_end_time": "2020-09-11T15:49:38.164565"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:55:40.104499"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:55:40.104499"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* button_need_help: I need help
    - utter_ca_aem_help_001   <!-- predicted: utter_pa_unsecured_choices -->
* transfer_to_expert: chat with expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## Story from conversation with 6942789b-761f-4095-86e6-35da42c9a484 on September 11th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-ab10d244-844c-4d29-bb33-ec41a4da6176"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "8135100988"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "959335288"}
    - slot{"first_name": "Jamille"}
    - action_pa_check
    - slot{"pa_status": "not_secured"}
    - slot{"pa_link": "https://t-mo.cc/mwfxv1lf9e"}
    - utter_pa_unsecured_choices   <!-- predicted: utter_pa_addpay_link -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
    - slot{"repeat_end_time": "2020-09-11T15:49:38.164565"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:55:40.104499"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:53:39.527356"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:55:40.104499"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* repeat: /repeat
    - action_pa_payment_check
    - slot{"pa_status": "not_secured"}
    - action_repeat
    - slot{"repeat_end_time": "2020-09-11T15:57:40.680918"}
* button_need_help: I need help
    - utter_ca_aem_help_001   <!-- predicted: utter_pa_unsecured_choices -->
* transfer_to_expert: chat with expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## Story from conversation with 29aa36b8-2ec2-4905-928d-c7fc3e8afe37 on October 14th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-09925b95-8fc6-4175-985b-d6bf66955d3a"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "4704434777"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "970267925"}
    - slot{"first_name": "Jessica"}
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - slot{"bill_pay_link": "https://t-mo.cc/26j3u0ou00"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* pa_create: Can I get a payment arrangement?
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "4704434777"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* transfer_to_expert: Chat with a live Expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## Story from conversation with 9830467c-6996-42da-b002-3bc796f86d89 on October 13th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-b7b386ce-16b9-4241-8621-9b570fa0cada"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "6822023279"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "899088234"}
    - slot{"first_name": "JOAN"}
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - slot{"pa_link": "https://t-mo.cc/82pdya0oc1"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* deny: No
    - utter_ca_aem_help_001   <!-- predicted: utter_pa_unsecured_choices -->
* transfer_to_expert: Chat with expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## Story from conversation with d234cb2b-ec5d-438f-83c6-65fb632062a1 on October 14th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-3523471a-560a-496c-9081-f5c5dc613cc6"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "8159098097"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "969455369"}
    - slot{"first_name": "Zeke"}
    - action_pa_check
    - slot{"pa_status": "ineligible"}
    - slot{"bill_pay_link": "https://t-mo.cc/w2egh7e3rp"}
    - utter_pa_ineligible   <!-- predicted: utter_ca_wm_01 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* bill_pay: manage my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_not_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_not_exists"}
    - utter_ca_bp_001_2   <!-- predicted: utter_broken -->


## Story from conversation with 3b66013b-3023-4ddd-8a83-6f6a6e395b99 on October 12th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-31655743-a7a9-45a3-8a7c-50286c8c4d09"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "8589270456"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "966493274"}
    - slot{"first_name": "Tadiyo"}
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - slot{"pa_link": "https://t-mo.cc/62tu0vdxrt"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* broken: Still can’t click it
    - utter_broken   <!-- predicted: utter_transfer_expert -->
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## Story from conversation with b17e6c07-22b9-40fd-8d8d-b92a99a1f6ea on September 29th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-6fe98842-374e-444d-871b-ffbfe90a1cf1"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"main_menu_skill": "1919068430"}
* pa_create: /pa_create
    - utter_welcome   <!-- predicted: utter_pa_pay_balance_due -->
    - action_customer_authentication
    - slot{"msisdn": "2672106937"}
    - slot{"auth_token": "ItIsAlwaysValidToken"}
    - action_customer_profile
    - slot{"ban": "957566844"}
    - slot{"first_name": "Meenah"}
    - action_pa_check
    - slot{"pa_status": "eligible"}
    - slot{"pa_link": "https://t-mo.cc/l6r1r601gf"}
    - utter_pa_eligible   <!-- predicted: utter_ca_shop_trade_001 -->
    - action_delay_2_minutes
* delay: /delay
    - action_pa_payment_check
    - slot{"pa_status": "eligible"}
    - utter_pa_ask_help   <!-- predicted: utter_ca_pa_001_45_transfer_padates -->
    - action_repeat_start
    - slot{"repeat_end_time": "2020-09-29T22:42:35.557687"}
* thank: Done thanks a bunch
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Auto Pay Setup = True and Past Due Balance = False and Pay full bill - Happy Path (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_not_exists"}
    - utter_ca_bp_001_30   <!-- predicted: utter_ca_bp_001_20a -->
    - utter_ca_bp_001_31   <!-- predicted: utter_ca_bp_001_3 -->
* button_link_pay_my_bill_now: /button_link_pay_my_bill_now
    - action_delay_5_minutes   <!-- predicted: action_delay_45_seconds -->
* delay: /delay
    - action_check_payment_amount_changed
    - slot{"payment_amount_changed": "changed"}
    - slot{"current_bill_amount": "30.50"}
    - slot{"account_balance": "0.00"}
    - utter_ca_bp_001_33   <!-- predicted: utter_ca_bp_001_30 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* button_text_transfer_to_survey: /button_text_transfer_to_survey
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## review plan (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_plan_options: Manage my plan and add-ons
    - utter_ca_ot_004_menu_plan   <!-- predicted: utter_ca_bp_credit_01 -->
* plan_review: Review my plan
    - utter_ca_ot_011_jump_reviewplan   <!-- predicted: utter_ca_ot_008_jump_shop -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Change or compare plan (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_plan_options: Manage my plan and add-ons
    - utter_ca_ot_004_menu_plan   <!-- predicted: utter_ca_bp_credit_01 -->
* plan_compare: Change or compare my plan
    - utter_ca_ot_012_jump_compareplan   <!-- predicted: utter_ca_ot_009_jump_autopay -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Update my data and add-on (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_plan_options: Manage my plan and add-ons
    - utter_ca_ot_004_menu_plan   <!-- predicted: utter_ca_bp_credit_01 -->
* plan_addons: Update my data or add-ons
    - utter_ca_ot_013_jump_dataplan   <!-- predicted: utter_ca_ot_010_jump_routepa -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## add on back to main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_plan_options: Manage my plan and add-ons
    - utter_ca_ot_004_menu_plan   <!-- predicted: utter_ca_bp_credit_01 -->
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


## Add new line (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_add_suspend: Add or suspend a line
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* line_add: Add new line to my account
    - utter_ca_ot_014_jump_aalnew   <!-- predicted: utter_ca_ot_011_jump_billing -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Buy your own device (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_add_suspend: Add or suspend a line
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* line_add_byo: Bring your own device
    - utter_ca_ot_015_jump_aal   <!-- predicted: utter_ca_ot_011_jump_reviewplan -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: no, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Temporarily suspend my line (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_add_suspend: Add or suspend a line
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* line_suspend: Temporarily suspend my line
    - utter_ca_ot_016_jump_suspend   <!-- predicted: utter_ca_ot_012_jump_compareplan -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Add or suspend a line back to main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_add_suspend: Add or suspend a line
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


## Report a lost or stolen phone (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* lost_phone: Report a lost or stolen phone
    - utter_ca_ot_007_jump_stolen   <!-- predicted: utter_ca_ot_003_menu_services -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## services to main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage my services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* main_menu: Main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


## Auto Pay Setup = True and Past Due Balance = False and View my bill - Happy Path (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_view: I want to view my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_not_exists"}
    - utter_ca_bp_001_30   <!-- predicted: utter_ca_bp_001_20a -->
    - utter_ca_bp_001_31   <!-- predicted: utter_ca_bp_001_3 -->
* button_link_view_my_bill: /button_link_view_my_bill
    - action_delay_5_minutes   <!-- predicted: action_delay_45_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Shop Apple devices (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: Main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* shop_device: Shop devices and pricing
    - utter_ca_ot_008_jump_shop   <!-- predicted: utter_ca_ot_005_menu_line -->
* button_shop_apple_device: Shop Apple devices
    - utter_ca_ot_018_jump_apple   <!-- predicted: utter_transfer_menu -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: no, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Shop other devices (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* shop_device: Shop devices and pricing
    - utter_ca_ot_008_jump_shop   <!-- predicted: utter_ca_ot_005_menu_line -->
* button_shop_other_device: Shop other devices
    - utter_ca_ot_019_jump_shop   <!-- predicted: utter_transfer_spanish -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Check order status (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: man menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* shop_device: Shop devices and pricing
    - utter_ca_ot_008_jump_shop   <!-- predicted: utter_ca_ot_005_menu_line -->
* order_status: Check order status
    - utter_ca_ot_020_jump_order_status   <!-- predicted: utter_transfer_survey -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* deny: No, thanks
    - utter_transfer_survey   <!-- predicted: utter_pa_paynow -->


## Shop devices to main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* shop_device: Shop devices and pricing
    - utter_ca_ot_008_jump_shop   <!-- predicted: utter_ca_ot_005_menu_line -->
* main_menu: Main Menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


## main menu to expert (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* transfer_to_expert: Chat with a live Expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## View or pay my bill (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* button_payment_options: View billing & payment options
    - utter_ca_ot_002_menu_billing   <!-- predicted: utter_ca_bp_apcredit_01 -->
* bill_pay: manage my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_not_exists"}
    - utter_ca_bp_001_30   <!-- predicted: utter_ca_bp_001_20a -->
    - utter_ca_bp_001_31   <!-- predicted: utter_ca_bp_001_3 -->


## Set up or manage my AutoPay (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->
* button_payment_options: View billing & payment options
    - utter_ca_ot_002_menu_billing   <!-- predicted: utter_ca_bp_apcredit_01 -->
* setup_autopay: Set up or manage my AutoPay
    - utter_ca_ot_009_jump_autopay   <!-- predicted: utter_ca_ot_006_menu_else -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## manage service to suspend line (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage Services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_add_suspend: Add or suspend a line
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* line_suspend: Suspend line
    - utter_ca_ot_016_jump_suspend   <!-- predicted: utter_ca_ot_012_jump_compareplan -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## direct suspend line (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* line_suspend: Suspend line
    - utter_ca_ot_016_jump_suspend   <!-- predicted: utter_ca_ot_012_jump_compareplan -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## manage service to add line (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_manage_services: Manage Services
    - utter_ca_ot_003_menu_services   <!-- predicted: utter_ca_bp_bill0_01 -->
* button_add_suspend: Add or suspend a line
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* line_add: Add new line
    - utter_ca_ot_014_jump_aalnew   <!-- predicted: utter_ca_ot_011_jump_billing -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Auto Pay Setup = True and Past Due Balance = True and Message a live expert (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I want to pay my last month bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_exists"}
    - utter_ca_bp_001_20   <!-- predicted: utter_ca_aem_help_001 -->
    - utter_ca_bp_001_20a   <!-- predicted: utter_ca_bp_001_2 -->
* button_text_transfer_to_expert: /button_text_transfer_to_expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## direct add line (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* line_add: I want to add a line to my account
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->


## Story from conversation with 20fdde3f-12a8-4fe2-a7d2-8866f1673afd on November 10th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "tmoweb"}
    - slot{"conversation_channel_id": "tmoweb_cfba29a8-61de-4810-ba29-a861de581045"}
    - slot{"conversation_sub_channel": "none"}
    - slot{"conversation_routing_group": "English"}
    - slot{"conversation_language": "en"}
    - slot{"conversation_topic": "na"}
    - slot{"survey_skill": "2023321130"}
    - slot{"care_skill": "2065085430"}
    - slot{"spanish_skill": "1946176930"}
* shop_device: /shop_device
    - utter_ca_ot_008_jump_shop   <!-- predicted: utter_ca_ot_005_menu_line -->


## Story from conversation with 253e2cec-28eb-4ff1-a87e-c1cdd425dca7 on November 10th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "tmoweb"}
    - slot{"conversation_channel_id": "tmoweb_cfba29a8-61de-4810-ba29-a861de581045"}
    - slot{"conversation_sub_channel": "none"}
    - slot{"conversation_routing_group": "English"}
    - slot{"conversation_language": "en"}
    - slot{"conversation_topic": "na"}
    - slot{"survey_skill": "2023321130"}
    - slot{"care_skill": "2065085430"}
    - slot{"spanish_skill": "1946176930"}
* plan_addons: /plan_addons
    - utter_ca_ot_013_jump_dataplan   <!-- predicted: utter_ca_ot_010_jump_routepa -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Story from conversation with d1db7056-9ceb-4860-9c92-3ba50403c935 on November 12th 2020 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
    - slot{"conversation_channel": "appweb"}
    - slot{"conversation_channel_id": "appweb_U-f4fa6f6b-85e4-48cf-b1a1-1363ee8db51c"}
    - slot{"conversation_sub_channel": "app"}
    - slot{"conversation_routing_group": "English"}
    - slot{"conversation_language": "en"}
    - slot{"conversation_topic": "na"}
    - slot{"survey_skill": "1963917230"}
    - slot{"care_skill": "1920509530"}
    - slot{"spanish_skill": "1926150830"}
* line_add: /line_add
    - utter_ca_ot_005_menu_line   <!-- predicted: utter_ca_ot_002_menu_billing -->
* line_add: Buy device for new line
    - utter_ca_ot_014_jump_aalnew   <!-- predicted: utter_ca_ot_011_jump_billing -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* button_need_help: I need help
    - utter_ca_aem_help_001   <!-- predicted: utter_pa_unsecured_choices -->
* transfer_to_expert: chat with expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## worry shutoff (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* worry_shutoff: I am scared my phone will be shut off
    - utter_ca_bp_001_worryshutoff   <!-- predicted: utter_pa_ask_help -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## transfer to expert on bill shock intent (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* bill_shock: I am being charged the wrong amount
    - utter_ca_bp_001_32   <!-- predicted: utter_ca_ot_014_jump_aalnew -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* button_text_transfer_to_expert: /button_text_transfer_to_expert
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## greet and main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* greeting: Hello
    - utter_ca_ot_021_greeting_menu   <!-- predicted: utter_trouble -->
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


## broken Can't accesss the website (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* broken: Can't accesss the website
    - utter_broken   <!-- predicted: utter_transfer_expert -->
    - action_customer_update_state
    - utter_route_expert   <!-- predicted: utter_pa_editpay_link -->
    - utter_transfer_expert   <!-- predicted: utter_pa_ineligible -->


## direct payment arrangement view (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* pa_view_existing: view payment arrangement
    - action_customer_authentication
    - action_customer_profile
    - action_pa_view
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## View Deals (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_view_deals: View all deals
    - utter_ca_shop_deals_001   <!-- predicted: utter_route_expert -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Auto Pay Setup = True and Past Due Balance = True and View my bill (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_view: I want to view my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_exists"}
    - utter_ca_bp_001_20   <!-- predicted: utter_ca_aem_help_001 -->
    - utter_ca_bp_001_20a   <!-- predicted: utter_ca_bp_001_2 -->
* button_link_view_my_bill: /button_link_view_my_bill
    - action_delay_5_minutes   <!-- predicted: action_delay_45_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Show Deals (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_view_deals: Show all deals
    - utter_ca_shop_deals_001   <!-- predicted: utter_route_expert -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Trade in options (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\7bea6c56feff4fb784d510f3171d60f3_conversation_tests.md)
* button_tradein: View trade in options
    - utter_ca_shop_trade_001   <!-- predicted: utter_route_menu -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->


## Auto Pay Setup = False and Account Balance = $0 (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I wanna pay my past due bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_not_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "account_balance_zero"}
    - utter_ca_bp_bill0_01   <!-- predicted: utter_ca_bp_001_32 -->


## Auto Pay Setup = False and Account Balance = Negative (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I wanna pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_not_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "account_balance_negative"}
    - utter_ca_bp_credit_01   <!-- predicted: utter_ca_bp_001_33 -->


## Auto Pay Setup = False and Past Due Balance = False, Pay My Bill and Main menu (C:\Users\hwensle1\AppData\Local\Temp\tmp74ielynl\cf921257f36646298275183668bfb63f_conversation_payment_tests.md)
* bill_pay: I would like to pay my bill
    - action_get_all_payment_links
    - action_customer_authentication
    - action_customer_profile
    - action_payment_get_autopay_info
    - slot{"payment_checks": "auto_pay_not_exists"}
    - action_payment_get_generalpayment_info
    - slot{"payment_checks": "past_due_balance_not_exists"}
    - utter_ca_bp_001_2   <!-- predicted: utter_broken -->
* button_link_pay_my_bill_now: /button_link_pay_my_bill_now
    - action_delay_5_minutes   <!-- predicted: action_delay_45_seconds -->
* delay: /delay
    - action_check_payment_amount_changed
    - slot{"payment_amount_changed": "changed"}
    - utter_ca_bp_001_33   <!-- predicted: utter_ca_bp_001_30 -->
    - action_delay_45_seconds   <!-- predicted: action_delay_5_seconds -->
* delay: /delay
    - utter_ca_ot_006_menu_else   <!-- predicted: utter_ca_ot_001_menu_main -->
* main_menu: main menu
    - utter_ca_ot_001_menu_main   <!-- predicted: utter_ca_bp_001_worryshutoff -->


