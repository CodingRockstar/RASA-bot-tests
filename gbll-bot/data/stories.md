## story_1010_norepeat
* greet
  - utter_greet
* affirm
  - utter_start
  - utter_iscustomer
* affirm
  - action_setslot_customer
  - slot{"iscustomer": "ja"}
  - utter_confirm
  - utter_hastext
* deny
  - action_setslot_hastext
  - slot{"hastext": "nein"}
  - utter_confirm
  - utter_truestatements
* affirm
  - action_setslot_truestatements
  - slot{"truestatements": "ja"}
  - utter_confirm
  - utter_offences
* deny
  - action_setslot_offences
  - slot{"offences": "nein"}
  - utter_confirm
  - utter_result_summary
  - action_rating_result
  - utter_ask_restart
* deny
  - utter_goodbye

## story_1010_repeat
* greet
  - utter_greet
* affirm
  - utter_start
  - utter_iscustomer
* affirm
  - action_setslot_customer
  - slot{"iscustomer": "ja"}
  - utter_confirm
  - utter_hastext
* deny
  - action_setslot_hastext
  - slot{"hastext": "nein"}
  - utter_confirm
  - utter_truestatements
* affirm
  - action_setslot_truestatements
  - slot{"truestatements": "ja"}
  - utter_confirm
  - utter_offences
* deny
  - action_setslot_offences
  - slot{"offences": "nein"}
  - utter_confirm
  - utter_result_summary
  - action_rating_result
  - utter_ask_restart
* affirm
  - action_chat_restart

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
