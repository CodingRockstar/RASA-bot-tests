## start denied
* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* deny
    - utter_goodbye

## unhappy path
* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name": "rating_form"}
* chitchat
    - utter_chitchat
    - rating_form
    - form{"name": null}
* thankyou
    - utter_welcome

## very unhappy path
* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name": "rating_form"}
* chitchat
    - utter_chitchat
    - rating_form
* chitchat
    - utter_chitchat
    - rating_form
* chitchat
    - utter_chitchat
    - rating_form
    - form{"name": null}
* thankyou
    - utter_welcome

## stop but continue path
* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name": "rating_form"}
* stop
    - utter_ask_continue
* affirm
    - rating_form
    - form{"name": "rating_form"}
* thankyou
    - utter_thankyou

## stop and really stop path
* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name": "rating_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_thankyou

## say goodbye
* goodbye
  - utter_goodbye
  - action_clear_slots

## bot challenge
* bot_challenge
  - utter_iamabot

## 1-0-1-1

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* deny OR hastext_deny
    - rating_form
    - slot{"hastext":"nein"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}

## 1-1-1-0

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* affirm OR hastext_affirm
    - rating_form
    - slot{"hastext":"ja"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* deny
    - rating_form
    - slot{"offences":"nein"}
    - form{"name":null}
    - slot{"requested_slot":null}

## 1-0-1-1

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* deny OR hastext_deny
    - rating_form
    - slot{"hastext":"nein"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}

## 1-0-1-0

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* deny OR hastext_deny
    - rating_form
    - slot{"hastext":"nein"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* deny
    - rating_form
    - slot{"offences":"nein"}
    - form{"name":null}
    - slot{"requested_slot":null}

## 1-0-1-2

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* deny OR hastext_deny
    - rating_form
    - slot{"hastext":"nein"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* unclear
    - rating_form
    - slot{"offences":"unklar"}
    - form{"name":null}
    - slot{"requested_slot":null}

## 1-1-1-1

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* affirm OR hastext_affirm
    - rating_form
    - slot{"hastext":"ja"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}

## 1-1-1-2

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* affirm OR hastext_affirm
    - rating_form
    - slot{"hastext":"ja"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* unclear
    - rating_form
    - slot{"offences":"unklar"}
    - form{"name":null}
    - slot{"requested_slot":null}

## stop - continue - stop - really stop

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* stop
    - utter_ask_continue
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_thankyou

## 1-1-1-1 w/ chitchat

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* get_started OR affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* chitchat
    - utter_chitchat
    - rating_form
    - slot{"requested_slot":"hastext"}
* affirm OR hastext_affirm
    - rating_form
    - slot{"hastext":"ja"}
    - slot{"requested_slot":"truestatements"}
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}

## developed by
* developedby
  - utter_developedby

## greet /w developed by & stop

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* developedby
    - utter_developedby
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_thankyou

## need help

* needhelp
    - utter_help

## 1-0-0-1 /w help

* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* needhelp
    - utter_help
    - utter_ask_continue
* affirm
    - rating_form
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* hastext_deny
    - rating_form
    - slot{"hastext":"nein"}
    - slot{"requested_slot":"truestatements"}
* deny
    - rating_form
    - slot{"truestatements":"nein"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thankyou
    - utter_thankyou
    - utter_goodbye

## insult at start

* insult
    - utter_insult
    - utter_goodbye
    - action_clear_slots
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}

## insult during process
* greet
    - utter_greet
    - utter_terms_of_service
    - utter_ask_start
* affirm
    - utter_start
    - action_clear_slots
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* deny
    - rating_form
    - slot{"hastext":"nein"}
    - slot{"requested_slot":"truestatements"}
* insult
    - utter_insult
    - utter_goodbye
    - action_clear_slots
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
