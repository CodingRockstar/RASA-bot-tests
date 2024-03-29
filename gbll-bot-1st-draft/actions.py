from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUttered, FollowupAction


"""
Class ActionSetslotCustomer
set slot iscustomer even for text inputs
when user answers question with input
"""
class ActionSetslotCustomer(Action):
    def name(self):
        return "action_setslot_customer"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        value = tracker.get_slot("iscustomer")

        if intent == 'affirm':
            return [SlotSet("iscustomer", "ja")]
        elif intent == 'deny':
            return [SlotSet("iscustomer", "nein")]
        else:
            return [SlotSet("iscustomer", value)]


"""
Class ActionSetslotHastext
set slot hastext even for text inputs
when user answers question with input
"""
class ActionSetslotHastext(Action):
    def name(self):
        return "action_setslot_hastext"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        value = tracker.get_slot("hastext")

        if intent == 'affirm':
            return [SlotSet("hastext", "ja")]
        elif intent == 'deny':
            return [SlotSet("hastext", "nein")]
        else:
            return [SlotSet("hastext", value)]


"""
Class ActionSetslotTruestatement
set slot truestatements even for text inputs
when user answers question with input
"""
class ActionSetslotTruestatement(Action):
    def name(self):
        return "action_setslot_truestatements"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        value = tracker.get_slot("truestatements")

        if intent == 'affirm':
            return [SlotSet("truestatements", "ja")]
        elif intent == 'deny':
            return [SlotSet("truestatements", "nein")]
        elif intent == 'unclear':
            return [SlotSet("truestatements", "unklar")]
        elif intent == 'indifferent':
            return [SlotSet("truestatements", "teilweise")]
        else:
            return [SlotSet("truestatements", value)]


"""
Class ActionSetslotOffences
set slot offences even for text inputs
when user answers question with input
"""
class ActionSetslotOffences(Action):
    def name(self):
        return "action_setslot_offences"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        value = tracker.get_slot("offences")

        if intent == 'affirm':
            return [SlotSet("offences", "ja")]
        elif intent == 'deny':
            return [SlotSet("offences", "nein")]
        elif intent == 'unclear':
            return [SlotSet("offences", "unklar")]
        else:
            return [SlotSet("offences", value)]


"""
Class ActionReturnRatingResult
set Slots to None and restart
"""
class ActionReturnRatingResult(Action):
    def name(self):
        return "action_rating_result"

    def run(self, dispatcher, tracker, domain):
        iscustomer = tracker.get_slot("iscustomer")
        hastext = tracker.get_slot("hastext")
        truestatements = tracker.get_slot("truestatements")
        offences = tracker.get_slot("offences")

        if iscustomer == "ja" and hastext == "ja" and truestatements == "ja" and offences == "nein":
            dispatcher.utter_message(template="utter_result_impossible")
        elif iscustomer == "ja" and hastext == "ja" and truestatements == "ja" and offences == "unklar":
            dispatcher.utter_message(template="utter_result_indifferent")
            dispatcher.utter_message(template="utter_result_gotolegalcase_process")
        else:
            dispatcher.utter_message(template="utter_result_success")
            dispatcher.utter_message(template="utter_result_gotolegalcase_process")

        return []


"""
Class ActionRestarted
set Slots to None and restart
"""
class ActionRestarted(Action):
    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [
            Restarted(),
            UserUttered(text="hi", parse_data={
                   "intent": {"confidence": 1.0, "name": "greet"},
                   "entities": []
                  }),
            FollowupAction(name="utter_iscustomer"),
        ]