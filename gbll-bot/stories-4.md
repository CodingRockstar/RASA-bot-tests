
## interactive_story_1
* greet
    - utter_greet
* affirm
    - utter_start
    - utter_iscustomer
* affirm{"iscustomer": "ja"}
    - slot{"iscustomer": "ja"}
    - action_setslot_customer
    - slot{"iscustomer": "ja"}
    - utter_confirm
    - utter_hastext
* deny{"hastext": "nein"}
    - slot{"hastext": "nein"}
    - action_setslot_hastext
    - slot{"hastext": "nein"}
    - utter_confirm
    - utter_truestatements
* affirm{"truestatements": "ja"}
    - slot{"truestatements": "ja"}
    - action_setslot_truestatements
    - slot{"truestatements": "ja"}
    - utter_confirm
    - utter_offences
* affirm{"offences": "ja"}
    - slot{"offences": "ja"}
    - action_setslot_offences
    - slot{"offences": "ja"}
    - utter_confirm
    - utter_result_summary
    - utter_result_success
    - utter_result_gotolegalcase_process
    - utter_ask_restart
* affirm
    - action_chat_restart

## interactive_story_2
* greet
    - followup{"name": "utter_greet"}
    - utter_greet
* affirm
    - utter_iscustomer
* affirm{"iscustomer": "ja"}
    - slot{"iscustomer": "ja"}
    - action_setslot_customer
    - slot{"iscustomer": "ja"}
    - utter_confirm
    - utter_hastext
* deny
    - action_setslot_hastext
    - slot{"hastext": "nein"}
    - utter_confirm
    - utter_truestatements
* affirm{"truestatements": "ja"}
    - slot{"truestatements": "ja"}
    - action_setslot_truestatements
    - slot{"truestatements": "ja"}
    - utter_confirm
    - utter_offences
* affirm{"offences": "ja"}
    - slot{"offences": "ja"}
    - action_setslot_offences
    - slot{"offences": "ja"}
    - utter_confirm
    - utter_result_summary
    - utter_result_success
    - utter_result_gotolegalcase_process
    - utter_ask_restart
* deny
    - utter_goodbye
