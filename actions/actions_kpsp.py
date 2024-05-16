from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction


class ActionFeedbackChecklistfirst(Action):
    def name(self):
        return "action_feedback_checklistfirst"

    def run(self, dispatcher, tracker, domain):

        question11 = tracker.get_slot("question11")
        question12 = tracker.get_slot("question12")
        question13 = tracker.get_slot("question13")
        question14 = tracker.get_slot("question14")
        question15 = tracker.get_slot("question15")
        question16 = tracker.get_slot("question16")
        question17 = tracker.get_slot("question17")
        question18 = tracker.get_slot("question18")
        question19 = tracker.get_slot("question19")
        question110 = tracker.get_slot("question110")
        
        
        if question11 == False:
            dispatcher.utter_message(response="utter_response_question11")
        if question12 == False:
            dispatcher.utter_message(response="utter_response_question12")
        if question13 == False:
            dispatcher.utter_message(response="utter_response_question13")
        if question14 == False:
            dispatcher.utter_message(response="utter_response_question14")
        if question15 == False:
            dispatcher.utter_message(response="utter_response_question15")
        if question16 == False:
            dispatcher.utter_message(response="utter_response_question16")
        if question17 == False:
            dispatcher.utter_message(response="utter_response_question17")
        if question18 == False:
            dispatcher.utter_message(response="utter_response_question18")
        if question19 == False:
            dispatcher.utter_message(response="utter_response_question19")
        if question110 == False:
            dispatcher.utter_message(response="utter_response_question110")
            
        return []
    
class ActionFeedbackChecklistsecond(Action):
    def name(self):
        return "action_feedback_checklistsecond"

    def run(self, dispatcher, tracker, domain):

        question21 = tracker.get_slot("question21")
        question22 = tracker.get_slot("question22")
        question23 = tracker.get_slot("question23")
        question24 = tracker.get_slot("question24")
        question25 = tracker.get_slot("question25")
        question26 = tracker.get_slot("question26")
        question27 = tracker.get_slot("question27")
        question28 = tracker.get_slot("question28")
        question29 = tracker.get_slot("question29")
        question210 = tracker.get_slot("question210")
                
        if question21 == False:
            dispatcher.utter_message(response="utter_response_question21")

        if question22 == False:
            dispatcher.utter_message(response="utter_response_question22")

        if question23 == False:
            dispatcher.utter_message(response="utter_response_question23")

        if question24 == False:
            dispatcher.utter_message(response="utter_response_question24")

        if question25 == False:
            dispatcher.utter_message(response="utter_response_question25")

        if question26 == False:
            dispatcher.utter_message(response="utter_response_question26")

        if question27 == False:
            dispatcher.utter_message(response="utter_response_question27")

        if question28 == False:
            dispatcher.utter_message(response="utter_response_question28")

        if question29 == False:
            dispatcher.utter_message(response="utter_response_question29")

        if question210 == False:
            dispatcher.utter_message(response="utter_response_question210")

        return []

class ActionFeedbackChecklistthird(Action):
    def name(self):
        return "action_feedback_checklistthird"

    def run(self, dispatcher, tracker, domain):

        question31 = tracker.get_slot("question31")
        question32 = tracker.get_slot("question32")
        question33 = tracker.get_slot("question33")
        question34 = tracker.get_slot("question34")
        question35 = tracker.get_slot("question35")
        question36 = tracker.get_slot("question36")
        question37 = tracker.get_slot("question37")
        question38 = tracker.get_slot("question38")
        question39 = tracker.get_slot("question39")
        question310 = tracker.get_slot("question310")

        if question31 == False:
            dispatcher.utter_message(response="utter_response_question31")

        if question32 == False:
            dispatcher.utter_message(response="utter_response_question32")

        if question33 == False:
            dispatcher.utter_message(response="utter_response_question33")

        if question34 == False:
            dispatcher.utter_message(response="utter_response_question34")

        if question35 == False:
            dispatcher.utter_message(response="utter_response_question35")

        if question36 == False:
            dispatcher.utter_message(response="utter_response_question36")

        if question37 == False:
            dispatcher.utter_message(response="utter_response_question37")

        if question38 == False:
            dispatcher.utter_message(response="utter_response_question38")

        if question39 == False:
            dispatcher.utter_message(response="utter_response_question39")

        if question310 == False:
            dispatcher.utter_message(response="utter_response_question310")

        return []
        
class ActionFeedbackChecklistfourth(Action):
    def name(self):
        return "action_feedback_checklistfourth"

    def run(self, dispatcher, tracker, domain):

        question41 = tracker.get_slot("question41")
        question42 = tracker.get_slot("question42")
        question43 = tracker.get_slot("question43")
        question44 = tracker.get_slot("question44")
        question45 = tracker.get_slot("question45")
        question46 = tracker.get_slot("question46")
        question47 = tracker.get_slot("question47")
        question48 = tracker.get_slot("question48")
        question49 = tracker.get_slot("question49")
        question410 = tracker.get_slot("question410")

        if question41 == False:
            dispatcher.utter_message(response="utter_response_question41")

        if question42 == False:
            dispatcher.utter_message(response="utter_response_question42")

        if question43 == False:
            dispatcher.utter_message(response="utter_response_question43")

        if question44 == False:
            dispatcher.utter_message(response="utter_response_question44")

        if question45 == False:
            dispatcher.utter_message(response="utter_response_question45")

        if question46 == False:
            dispatcher.utter_message(response="utter_response_question46")

        if question47 == False:
            dispatcher.utter_message(response="utter_response_question47")

        if question48 == False:
            dispatcher.utter_message(response="utter_response_question48")

        if question49 == False:
            dispatcher.utter_message(response="utter_response_question49")

        if question410 == False:
            dispatcher.utter_message(response="utter_response_question410")

        return []

class ActionFeedbackChecklistfifth(Action):
    def name(self):
        return "action_feedback_checklistfifth"

    def run(self, dispatcher, tracker, domain):

        question51 = tracker.get_slot("question51")
        question52 = tracker.get_slot("question52")
        question53 = tracker.get_slot("question53")
        question54 = tracker.get_slot("question54")
        question55 = tracker.get_slot("question55")
        question56 = tracker.get_slot("question56")
        question57 = tracker.get_slot("question57")
        question58 = tracker.get_slot("question58")
        question59 = tracker.get_slot("question59")
        question510 = tracker.get_slot("question510")

        if question51 == False:
            dispatcher.utter_message(response="utter_response_question51")

        if question52 == False:
            dispatcher.utter_message(response="utter_response_question52")

        if question53 == False:
            dispatcher.utter_message(response="utter_response_question53")

        if question54 == False:
            dispatcher.utter_message(response="utter_response_question54")

        if question55 == False:
            dispatcher.utter_message(response="utter_response_question55")

        if question56 == False:
            dispatcher.utter_message(response="utter_response_question56")

        if question57 == False:
            dispatcher.utter_message(response="utter_response_question57")

        if question58 == False:
            dispatcher.utter_message(response="utter_response_question58")

        if question59 == False:
            dispatcher.utter_message(response="utter_response_question59")

        if question510 == False:
            dispatcher.utter_message(response="utter_response_question510")

        return []
        

class ActionFeedbackChecklistsixth(Action):
    def name(self):
        return "action_feedback_checklistsixth"

    def run(self, dispatcher, tracker, domain):

        question61 = tracker.get_slot("question61")
        question62 = tracker.get_slot("question62")
        question63 = tracker.get_slot("question63")
        question64 = tracker.get_slot("question64")
        question65 = tracker.get_slot("question65")
        question66 = tracker.get_slot("question66")
        question67 = tracker.get_slot("question67")
        question68 = tracker.get_slot("question68")
        question69 = tracker.get_slot("question69")
        question610 = tracker.get_slot("question610")

        if question61 == False:
            dispatcher.utter_message(response="utter_response_question61")

        if question62 == False:
            dispatcher.utter_message(response="utter_response_question62")

        if question63 == False:
            dispatcher.utter_message(response="utter_response_question63")

        if question64 == False:
            dispatcher.utter_message(response="utter_response_question64")

        if question65 == False:
            dispatcher.utter_message(response="utter_response_question65")

        if question66 == False:
            dispatcher.utter_message(response="utter_response_question66")

        if question67 == False:
            dispatcher.utter_message(response="utter_response_question67")

        if question68 == False:
            dispatcher.utter_message(response="utter_response_question68")

        if question69 == False:
            dispatcher.utter_message(response="utter_response_question69")

        if question610 == False:
            dispatcher.utter_message(response="utter_response_question610")

        return []

class ActionFeedbackChecklistseventh(Action):
    def name(self):
        return "action_feedback_checklistseventh"

    def run(self, dispatcher, tracker, domain):

        question71 = tracker.get_slot("question71")
        question72 = tracker.get_slot("question72")
        question73 = tracker.get_slot("question73")
        question74 = tracker.get_slot("question74")
        question75 = tracker.get_slot("question75")
        question76 = tracker.get_slot("question76")
        question77 = tracker.get_slot("question77")
        question78 = tracker.get_slot("question78")
        question79 = tracker.get_slot("question79")
        question710 = tracker.get_slot("question710")

        if question71 == False:
            dispatcher.utter_message(response="utter_response_question71")

        if question72 == False:
            dispatcher.utter_message(response="utter_response_question72")

        if question73 == False:
            dispatcher.utter_message(response="utter_response_question73")

        if question74 == False:
            dispatcher.utter_message(response="utter_response_question74")

        if question75 == False:
            dispatcher.utter_message(response="utter_response_question75")

        if question76 == False:
            dispatcher.utter_message(response="utter_response_question76")

        if question77 == False:
            dispatcher.utter_message(response="utter_response_question77")

        if question78 == False:
            dispatcher.utter_message(response="utter_response_question78")

        if question79 == False:
            dispatcher.utter_message(response="utter_response_question79")

        if question710 == False:
            dispatcher.utter_message(response="utter_response_question710")

        return []

class ActionFeedbackChecklisteighth(Action):
    def name(self):
        return "action_feedback_checklisteighth"

    def run(self, dispatcher, tracker, domain):

        question81 = tracker.get_slot("question81")
        question82 = tracker.get_slot("question82")
        question83 = tracker.get_slot("question83")
        question84 = tracker.get_slot("question84")
        question85 = tracker.get_slot("question85")
        question86 = tracker.get_slot("question86")
        question87 = tracker.get_slot("question87")
        question88 = tracker.get_slot("question88")
        question89 = tracker.get_slot("question89")
        question810 = tracker.get_slot("question810")

        if question81 == False:
            dispatcher.utter_message(response="utter_response_question81")

        if question82 == False:
            dispatcher.utter_message(response="utter_response_question82")

        if question83 == False:
            dispatcher.utter_message(response="utter_response_question83")

        if question84 == False:
            dispatcher.utter_message(response="utter_response_question84")

        if question85 == False:
            dispatcher.utter_message(response="utter_response_question85")

        if question86 == False:
            dispatcher.utter_message(response="utter_response_question86")

        if question87 == False:
            dispatcher.utter_message(response="utter_response_question87")

        if question88 == False:
            dispatcher.utter_message(response="utter_response_question88")

        if question89 == False:
            dispatcher.utter_message(response="utter_response_question89")

        if question810 == False:
            dispatcher.utter_message(response="utter_response_question810")

        return []

class ActionFeedbackChecklistninth(Action):
    def name(self):
        return "action_feedback_checklistninth"

    def run(self, dispatcher, tracker, domain):

        question91 = tracker.get_slot("question91")
        question92 = tracker.get_slot("question92")
        question93 = tracker.get_slot("question93")
        question94 = tracker.get_slot("question94")
        question95 = tracker.get_slot("question95")
        question96 = tracker.get_slot("question96")
        question97 = tracker.get_slot("question97")
        question98 = tracker.get_slot("question98")
        question99 = tracker.get_slot("question99")
        question910 = tracker.get_slot("question910")

        if question91 == False:
            dispatcher.utter_message(response="utter_response_question91")

        if question92 == False:
            dispatcher.utter_message(response="utter_response_question92")

        if question93 == False:
            dispatcher.utter_message(response="utter_response_question93")

        if question94 == False:
            dispatcher.utter_message(response="utter_response_question94")

        if question95 == False:
            dispatcher.utter_message(response="utter_response_question95")

        if question96 == False:
            dispatcher.utter_message(response="utter_response_question96")

        if question97 == False:
            dispatcher.utter_message(response="utter_response_question97")

        if question98 == False:
            dispatcher.utter_message(response="utter_response_question98")

        if question99 == False:
            dispatcher.utter_message(response="utter_response_question99")

        if question910 == False:
            dispatcher.utter_message(response="utter_response_question910")

        return []

class ActionFeedbackChecklisttenth(Action):
    def name(self):
        return "action_feedback_checklisttenth"

    def run(self, dispatcher, tracker, domain):

        question101 = tracker.get_slot("question101")
        question102 = tracker.get_slot("question102")
        question103 = tracker.get_slot("question103")
        question104 = tracker.get_slot("question104")
        question105 = tracker.get_slot("question105")
        question106 = tracker.get_slot("question106")
        question107 = tracker.get_slot("question107")
        question108 = tracker.get_slot("question108")
        question109 = tracker.get_slot("question109")
        question1010 = tracker.get_slot("question1010")

        if question101 == False:
            dispatcher.utter_message(response="utter_response_question101")

        if question102 == False:
            dispatcher.utter_message(response="utter_response_question102")

        if question103 == False:
            dispatcher.utter_message(response="utter_response_question103")

        if question104 == False:
            dispatcher.utter_message(response="utter_response_question104")

        if question105 == False:
            dispatcher.utter_message(response="utter_response_question105")

        if question106 == False:
            dispatcher.utter_message(response="utter_response_question106")

        if question107 == False:
            dispatcher.utter_message(response="utter_response_question107")

        if question108 == False:
            dispatcher.utter_message(response="utter_response_question108")

        if question109 == False:
            dispatcher.utter_message(response="utter_response_question109")

        if question1010 == False:
            dispatcher.utter_message(response="utter_response_question1010")

        return []

class ActionFeedbackChecklisteleventh(Action):
    def name(self):
        return "action_feedback_checklisteleventh"

    def run(self, dispatcher, tracker, domain):

        question111 = tracker.get_slot("question111")
        question112 = tracker.get_slot("question112")
        question113 = tracker.get_slot("question113")
        question114 = tracker.get_slot("question114")
        question115 = tracker.get_slot("question115")
        question116 = tracker.get_slot("question116")
        question117 = tracker.get_slot("question117")
        question118 = tracker.get_slot("question118")
        question119 = tracker.get_slot("question119")

        if question111 == False:
            dispatcher.utter_message(response="utter_response_question111")

        if question112 == False:
            dispatcher.utter_message(response="utter_response_question112")

        if question113 == False:
            dispatcher.utter_message(response="utter_response_question113")

        if question114 == False:
            dispatcher.utter_message(response="utter_response_question114")

        if question115 == False:
            dispatcher.utter_message(response="utter_response_question115")

        if question116 == False:
            dispatcher.utter_message(response="utter_response_question116")

        if question117 == False:
            dispatcher.utter_message(response="utter_response_question117")

        if question118 == False:
            dispatcher.utter_message(response="utter_response_question118")

        if question119 == False:
            dispatcher.utter_message(response="utter_response_question119")

        return []