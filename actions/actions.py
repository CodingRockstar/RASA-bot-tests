from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUttered, FollowupAction
from rasa_sdk.forms import FormAction

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List


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
            FollowupAction(name="utter_ask_iscustomer"),
        ]


class RatingForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "rating_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["iscustomer", "hastext", "truestatements", "offences"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "iscustomer": [
                self.from_entity(entity="iscustomer"),
                self.from_intent(intent="affirm", value="ja"),
                self.from_intent(intent="deny", value="nein"),
                self.from_intent(intent="unclear", value="unklar")
            ],
            "hastext": [
                self.from_entity(entity="hastext"),
                self.from_intent(intent="affirm", value="ja"),
                self.from_intent(intent="deny", value="nein"),
                self.from_intent(intent="hastext_affirm", value="ja"),
                self.from_intent(intent="hastext_deny", value="nein")
            ],
            "truestatements": [
                self.from_entity(entity="truestatemens"),
                self.from_intent(intent="affirm", value="ja"),
                self.from_intent(intent="deny", value="nein"),
                self.from_intent(intent="indifferent", value="teilweise"),
                self.from_intent(intent="unclear", value="unklar")
            ],
            "offences": [
                self.from_entity(entity="offences"),
                self.from_intent(intent="affirm", value="ja"),
                self.from_intent(intent="deny", value="nein"),
                self.from_intent(intent="unclear", value="unklar")
            ]
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        iscustomer = tracker.get_slot("iscustomer")
        hastext = tracker.get_slot("hastext")
        truestatements = tracker.get_slot("truestatements")
        offences = tracker.get_slot("offences")

        if iscustomer == "ja" and hastext == "ja" and truestatements == "ja" and offences == "nein":
            dispatcher.utter_message(template="utter_result_impossible")
        elif (
                (iscustomer == "ja" and hastext == "ja" and truestatements == "ja" and offences == "unklar") or 
                (iscustomer == "ja" and hastext == "ja" and truestatements == "unklar" and offences == "nein") or 
                (iscustomer == "ja" and hastext == "ja" and truestatements == "unklar" and offences == "unklar") or
                (iscustomer == "unklar" and hastext == "ja" and truestatements == "ja" and offences == "nein") or
                (iscustomer == "unklar" and hastext == "ja" and truestatements == "ja" and offences == "unklar") or
                (iscustomer == "unklar" and hastext == "ja" and truestatements == "unklar" and offences == "nein") or
                (iscustomer == "unklar" and hastext == "ja" and truestatements == "unklar" and offences == "unklar")
            ):
            dispatcher.utter_message(template="utter_result_indifferent")
            dispatcher.utter_message(template="utter_result_gotolegalcase_process")
        else:
            dispatcher.utter_message(template="utter_result_success")
            dispatcher.utter_message(template="utter_result_gotolegalcase_process")

        return [AllSlotsReset()]


"""
Class ActionClearSlots
set Slots to None and restart
"""
class ActionClearSlots(Action):
    def name(self):
        return "action_clear_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]