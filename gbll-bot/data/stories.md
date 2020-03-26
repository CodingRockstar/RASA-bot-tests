## story_1011_stop
* greet
  - utter_greet
* affirm
  - utter_start
  - utter_iscustomer
* affirm
  - action_setslot_customer
  - utter_confirm
  - utter_hastext
* deny
  - action_setslot_hastext
  - utter_confirm
  - utter_truestatements
* affirm
  - action_setslot_truestatements
  - utter_confirm
  - utter_offences
* affirm
  - action_setslot_offences
  - utter_confirm
  - utter_result_summary
  - utter_result_success
  - utter_ask_restart
* deny
  - utter_goodbye

## story_1011_restart
* greet
  - utter_greet
* affirm
  - utter_start
  - utter_iscustomer
* affirm
  - action_setslot_customer
  - utter_confirm
  - utter_hastext
* deny
  - action_setslot_hastext
  - utter_confirm
  - utter_truestatements
* affirm
  - action_setslot_truestatements
  - utter_confirm
  - utter_offences
* affirm
  - action_setslot_offences
  - utter_confirm
  - utter_result_summary
  - utter_result_success
  - utter_ask_restart
* affirm
  - action_chat_restart
  - utter_greet

## start denied
* greet
  - utter_greet
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
