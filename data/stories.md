## happy path
* greet
    - utter_greet
* get_started OR affirm
    - utter_start
    - rating_form
    - form{"name": "rating_form"}
    - form{"name": null}
    - utter_goodbye
* thankyou
    - utter_welcome

## start denied
* greet
    - utter_greet
* deny
    - utter_goodbye

## unhappy path
* greet
    - utter_greet
* get_started OR affirm
    - utter_start
    - rating_form
    - form{"name": "rating_form"}
* chitchat
    - utter_chitchat
    - rating_form
    - form{"name": null}
* thankyou
    - utter_welcome
    - utter_goodbye

## very unhappy path
* greet
    - utter_greet
* get_started OR affirm
    - utter_start
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
    - utter_goodbye

## stop but continue path
* greet
    - utter_greet
* get_started OR affirm
    - utter_start
    - rating_form
    - form{"name": "rating_form"}
* stop
    - utter_ask_continue
* affirm
    - rating_form
    - form{"name": null}
* thankyou
    - utter_thankyou
    - utter_goodbye

## stop and really stop path
* greet
    - utter_greet
* get_started OR affirm
    - utter_start
    - rating_form
    - form{"name": "rating_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_thankyou
    - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
* get_started
    - utter_start
    - rating_form
    - form{"name": "rating_form"}
    - form{"name": null}
    - utter_goodbye
* thankyou
    - utter_welcome

## New Story

* greet
    - utter_greet
* affirm
    - utter_start
    - rating_form
    - form{"name": "rating_form"}
    - form{"name": null}
    - utter_goodbye
* thankyou
    - utter_welcome

## New Story

* greet
    - utter_greet
* affirm
    - utter_start
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
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* get_started
    - utter_start
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* affirm
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
    - utter_goodbye

## New Story

* greet
    - utter_greet
* affirm
    - utter_start
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
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* affirm
    - rating_form
    - slot{"offences":"ja"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* get_started
    - utter_start
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
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* deny
    - rating_form
    - slot{"offences":"nein"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* affirm
    - utter_start
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
* affirm
    - rating_form
    - slot{"truestatements":"ja"}
    - slot{"requested_slot":"offences"}
* unclear
    - rating_form
    - slot{"offences":"unklar"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* get_started
    - utter_start
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* affirm
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
    - utter_goodbye

## New Story

* greet
    - utter_greet
* affirm
    - utter_start
    - rating_form
    - form{"name":"rating_form"}
    - slot{"requested_slot":"iscustomer"}
* affirm
    - rating_form
    - slot{"iscustomer":"ja"}
    - slot{"requested_slot":"hastext"}
* affirm
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
    - utter_goodbye
