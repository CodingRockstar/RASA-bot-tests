# happy path
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

## start denied
* greet
    - utter_greet
* deny
    - utter_goodbye

## unhappy path
* greet
    - utter_greet
* get_started
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
* get_started
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
* get_started
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
* get_started
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
