# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
     

class ActionDataBeratbadanWanita(Action):
    def name(self):
        return "action_data_beratbadan_wanita"

    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        umur = float(tracker.get_slot("umur"))
        berat_badan = float(tracker.get_slot("berat_badan"))
            
        if umur == 0:
            median = 3.2
            if berat_badan < median:
                nsbr = 2.8
            elif berat_badan > median:
                nsbr = 3.7
            else:
                nsbr = median
        elif umur == 1:
            median = 4.2
            if berat_badan < median:
                nsbr = 3.6
            elif berat_badan > median:
                nsbr = 4.8
            else:
                nsbr = median
        elif umur == 2:
            median = 5.1
            if berat_badan < median:
                nsbr = 4.5
            elif berat_badan > median:
                nsbr = 5.8
            else:
                nsbr = median
        elif umur == 3:
            median = 5.8
            if berat_badan < median:
                nsbr = 5.2
            elif berat_badan > median:
                nsbr = 6.6
            else:
                nsbr = median
        elif umur == 4:
            median = 6.4
            if berat_badan < median:
                nsbr = 5.7
            elif berat_badan > median:
                nsbr = 7.3
            else:
                nsbr = median
        elif umur == 5:
            median = 6.9
            if berat_badan < median:
                nsbr = 6.1
            elif berat_badan > median:
                nsbr = 7.8
            else:
                nsbr = median
        elif umur == 6:
            median = 7.3
            if berat_badan < median:
                nsbr = 6.5
            elif berat_badan > median:
                nsbr = 8.2
            else:
                nsbr = median
        elif umur == 7:
            median = 7.6
            if berat_badan < median:
                nsbr = 6.8
            elif berat_badan > median:
                nsbr = 8.6
            else:
                nsbr = median
        elif umur == 8:
            median = 7.9
            if berat_badan < median:
                nsbr = 7
            elif berat_badan > median:
                nsbr = 9
            else:
                nsbr = median
        elif umur == 9:
            median = 8.2
            if berat_badan < median:
                nsbr = 7.3
            elif berat_badan > median:
                nsbr = 9.3
            else:
                nsbr = median
        elif umur == 10:
            median = 8.5
            if berat_badan < median:
                nsbr = 7.5
            elif berat_badan > median:
                nsbr = 9.6
            else:
                nsbr = median
        elif umur == 11:
            median = 8.7
            if berat_badan < median:
                nsbr = 7.7
            elif berat_badan > median:
                nsbr = 9.9
            else:
                nsbr = median
        elif umur == 12:
            median = 8.9
            if berat_badan < median:
                nsbr = 7.9
            elif berat_badan > median:
                nsbr = 10.1
            else:
                nsbr = median
        elif umur == 13:
            median = 9.2
            if berat_badan < median:
                nsbr = 8.1
            elif berat_badan > median:
                nsbr = 10.4
            else:
                nsbr = median
        elif umur == 14:
            median = 9.4
            if berat_badan < median:
                nsbr = 8.3
            elif berat_badan > median:
                nsbr = 10.6
            else:
                nsbr = median
        elif umur == 15:
            median = 9.6
            if berat_badan < median:
                nsbr = 8.5
            elif berat_badan > median:
                nsbr = 10.9
            else:
                nsbr = median
        elif umur == 16:
            median = 9.8
            if berat_badan < median:
                nsbr = 8.7
            elif berat_badan > median:
                nsbr = 11.1
            else:
                nsbr = median
        elif umur == 17:
            median = 10
            if berat_badan < median:
                nsbr = 8.9
            elif berat_badan > median:
                nsbr = 11.4
            else:
                nsbr = median
        elif umur == 18:
            median = 10.2
            if berat_badan < median:
                nsbr = 9.1
            elif berat_badan > median:
                nsbr = 11.6
            else:
                nsbr = median
        elif umur == 19:
            median = 10.4
            if berat_badan < median:
                nsbr = 9.2
            elif berat_badan > median:
                nsbr = 11.8
            else:
                nsbr = median
        elif umur == 20:
            median = 10.6
            if berat_badan < median:
                nsbr = 9.4
            elif berat_badan > median:
                nsbr = 12.1
            else:
                nsbr = median
        elif umur == 21:
            median = 10.9
            if berat_badan < median:
                nsbr = 9.6
            elif berat_badan > median:
                nsbr = 12.3
            else:
                nsbr = median
        elif umur == 22:
            median = 11.1
            if berat_badan < median:
                nsbr = 9.8
            elif berat_badan > median:
                nsbr = 12.5
            else:
                nsbr = median
        elif umur == 23:
            median = 11.3
            if berat_badan < median:
                nsbr = 10
            elif berat_badan > median:
                nsbr = 12.8
            else:
                nsbr = median
        elif umur == 24:
            median = 11.5
            if berat_badan < median:
                nsbr = 10.2
            elif berat_badan > median:
                nsbr = 13
            else:
                nsbr = median
        elif umur == 25:
            median = 11.7
            if berat_badan < median:
                nsbr = 10.3
            elif berat_badan > median:
                nsbr = 13.3
            else:
                nsbr = median
        elif umur == 26:
            median = 11.9
            if berat_badan < median:
                nsbr = 10.5
            elif berat_badan > median:
                nsbr = 13.5
            else:
                nsbr = median
        elif umur == 27:
            median = 12.1
            if berat_badan < median:
                nsbr = 10.7
            elif berat_badan > median:
                nsbr = 13.7
            else:
                nsbr = median
        elif umur == 28:
            median = 12.3
            if berat_badan < median:
                nsbr = 10.9
            elif berat_badan > median:
                nsbr = 14
            else:
                nsbr = median
        elif umur == 29:
            median = 12.5
            if berat_badan < median:
                nsbr = 11.1
            elif berat_badan > median:
                nsbr = 14.2
            else:
                nsbr = median
        elif umur == 30:
            median = 12.7
            if berat_badan < median:
                nsbr = 11.2
            elif berat_badan > median:
                nsbr = 14.4
            else:
                nsbr = median
        elif umur == 31:
            median = 12.9
            if berat_badan < median:
                nsbr = 11.4
            elif berat_badan > median:
                nsbr = 14.7
            else:
                nsbr = median
        elif umur == 32:
            median = 13.1
            if berat_badan < median:
                nsbr = 11.6
            elif berat_badan > median:
                nsbr = 14.9
            else:
                nsbr = median
        elif umur == 33:
            median = 13.3
            if berat_badan < median:
                nsbr = 11.7
            elif berat_badan > median:
                nsbr = 15.1
            else:
                nsbr = median
        elif umur == 34:
            median = 13.5
            if berat_badan < median:
                nsbr = 11.9
            elif berat_badan > median:
                nsbr = 15.4
            else:
                nsbr = median
        elif umur == 35:
            median = 13.7
            if berat_badan < median:
                nsbr = 12
            elif berat_badan > median:
                nsbr = 15.6
            else:
                nsbr = median
        elif umur == 36:
            median = 13.9
            if berat_badan < median:
                nsbr = 12.2
            elif berat_badan > median:
                nsbr = 15.8
            else:
                nsbr = median
        elif umur == 37:
            median = 14
            if berat_badan < median:
                nsbr = 12.4
            elif berat_badan > median:
                nsbr = 16
            else:
                nsbr = median
        elif umur == 38:
            median = 14.2
            if berat_badan < median:
                nsbr = 12.5
            elif berat_badan > median:
                nsbr = 16.3
            else:
                nsbr = median
        elif umur == 39:
            median = 14.4
            if berat_badan < median:
                nsbr = 12.7
            elif berat_badan > median:
                nsbr = 16.5
            else:
                nsbr = median
        elif umur == 40:
            median = 14.6
            if berat_badan < median:
                nsbr = 12.8
            elif berat_badan > median:
                nsbr = 16.7
            else:
                nsbr = median
        elif umur == 41:
            median = 14.8
            if berat_badan < median:
                nsbr = 13
            elif berat_badan > median:
                nsbr = 16.9
            else:
                nsbr = median
        elif umur == 42:
            median = 15
            if berat_badan < median:
                nsbr = 13.1
            elif berat_badan > median:
                nsbr = 17.2
            else:
                nsbr = median
        elif umur == 43:
            median = 15.2
            if berat_badan < median:
                nsbr = 13.3
            elif berat_badan > median:
                nsbr = 17.4
            else:
                nsbr = median
        elif umur == 44:
            median = 15.3
            if berat_badan < median:
                nsbr = 13.4
            elif berat_badan > median:
                nsbr = 17.6
            else:
                nsbr = median
        elif umur == 45:
            median = 15.5
            if berat_badan < median:
                nsbr = 13.6
            elif berat_badan > median:
                nsbr = 17.8
            else:
                nsbr = median
        elif umur == 46:
            median = 15.7
            if berat_badan < median:
                nsbr = 13.7
            elif berat_badan > median:
                nsbr = 18.1
            else:
                nsbr = median
        elif umur == 47:
            median = 15.9
            if berat_badan < median:
                nsbr = 13.9
            elif berat_badan > median:
                nsbr = 18.3
            else:
                nsbr = median
        elif umur == 48:
            median = 16.1
            if berat_badan < median:
                nsbr = 14
            elif berat_badan > median:
                nsbr = 18.5
            else:
                nsbr = median
        elif umur == 49:
            median = 16.3
            if berat_badan < median:
                nsbr = 14.2
            elif berat_badan > median:
                nsbr = 18.8
            else:
                nsbr = median
        elif umur == 50:
            median = 16.4
            if berat_badan < median:
                nsbr = 14.3
            elif berat_badan > median:
                nsbr = 19
            else:
                nsbr = median
        elif umur == 51:
            median = 16.6
            if berat_badan < median:
                nsbr = 14.5
            elif berat_badan > median:
                nsbr = 19.2
            else:
                nsbr = median
        elif umur == 52:
            median = 16.8
            if berat_badan < median:
                nsbr = 14.6
            elif berat_badan > median:
                nsbr = 19.4
            else:
                nsbr = median
        elif umur == 53:
            median = 17
            if berat_badan < median:
                nsbr = 14.8
            elif berat_badan > median:
                nsbr = 19.7
            else:
                nsbr = median
        elif umur == 54:
            median = 17.2
            if berat_badan < median:
                nsbr = 14.9
            elif berat_badan > median:
                nsbr = 19.9
            else:
                nsbr = median
        elif umur == 55:
            median = 17.3
            if berat_badan < median:
                nsbr = 15.1
            elif berat_badan > median:
                nsbr = 20.1
            else:
                nsbr = median
        elif umur == 56:
            median = 17.5
            if berat_badan < median:
                nsbr = 15.2
            elif berat_badan > median:
                nsbr = 20.3
            else:
                nsbr = median
        elif umur == 57:
            median = 17.7
            if berat_badan < median:
                nsbr = 15.3
            elif berat_badan > median:
                nsbr = 20.6
            else:
                nsbr = median
        elif umur == 58:
            median = 17.9
            if berat_badan < median:
                nsbr = 15.5
            elif berat_badan > median:
                nsbr = 20.8
            else:
                nsbr = median
        elif umur == 59:
            median = 18
            if berat_badan < median:
                nsbr = 15.6
            elif berat_badan > median:
                nsbr = 21
            else:
                nsbr = median
        elif umur == 60:
            median = 18.2
            if berat_badan < median:
                nsbr = 15.8
            elif berat_badan > median:
                nsbr = 21.2
            else:
                nsbr = median
        else:
            dispatcher.utter_message(text="Data yang Anda masukkan tidak valid (Error: Umur harus tidak lebih  dari 60 bulan).")

        if berat_badan < median:
            zscore = (berat_badan - median) / (median - nsbr)
        else:
            zscore = (berat_badan - median) / (nsbr - median)

        dispatcher.utter_message(text="Data berat badan anak Anda: \n 1. Jenis Kelamin: Perempuan \n 2. Umur: " + str(umur) + " bulan" + "\n" "3. Berat Badan:" + str(berat_badan) + " kg")

        if zscore < -3:
            dispatcher.utter_message(text="Kategori: Berat badan sangat kurang (severely underweight)\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore >= -3 and zscore <= -2:
            dispatcher.utter_message(text="Kategori: Berat badan kurang (underweight)\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore > -2 and zscore <= 1:
            dispatcher.utter_message(text="Kategori: Berat badan normal\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore > 1:
            dispatcher.utter_message(text="Kategori: Risiko berat badan lebih\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")

        if umur > 0 and umur <= 24:
            dispatcher.utter_message(image="https://i.ibb.co/Mchtpg0/image.png")
        else:
            dispatcher.utter_message(image="https://i.ibb.co/ZVskfXm/image.png")

        return []
        # if umur == 0:
        #     if berat_badan > 0 and berat_badan <= 2.1:
        #         dispatcher.utter_message(text="Kategori: Berat badan sangat kurang (severely underweight)")
        #     elif berat_badan > 2.1 and berat_badan <= 2.5:
        #         dispatcher.utter_message(text="Kategori: Berat badan kurang (underweight)")
        #     elif berat_badan > 2.5 and berat_badan <= 3.9:
        #         dispatcher.utter_message(text="Kategori: Berat badan normal")
        #     elif berat_badan > 3.9:
        #         dispatcher.utter_message(text="Kategori: Risiko berat badan lebih")
        # else: 
        #     dispatcher.utter_message(text="Invalid input!")

        # if umur == 0 and berat_badan == 0:
        #     dispatcher.utter_message(text="Invalid input!")
        # elif umur == 0 and (berat_badan > 0 & berat_badan <= 2.1):
        #     dispatcher.utter_message(text="Kategori: Berat badan sangat kurang (severely underweight)")
        # elif umur == 0 and (berat_badan > 2.1 & berat_badan <= 2.5):
        #     dispatcher.utter_message(text="Kategori: Berat badan kurang (underweight)")
        # elif umur == 0 and (berat_badan > 2.5 & berat_badan <= 3.9):
        #     dispatcher.utter_message(text="Kategori: Berat badan normal")
        # elif umur == 0 and berat_badan > 3.9:
        #     dispatcher.utter_message(text="Kategori: Risiko berat badan lebih")




# class ValidateChecklistfirstForm(FormValidationAction):
#   def name(self) -> Text:
#       return "validate_checklistfirst_form"

#   @staticmethod
#   def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ):

#         question11 = tracker.get_slot("question11")

#         if question11 == False:
#             return [dispatcher.utter_message(text="Q1 Tidak Normal")]

#         return []

# class ActionSetChecklist(Action):
#     def name(self):
#         return "action_set_checklist"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         intent = tracker.latest_message["intent"].get("name")

#         if intent == "deny":
#             return [dispatcher.utter_message(text="Tidak Normal")]
#         elif intent == "affirm":
#             return [dispatcher.utter_message(text="Normal")]
#         return []
    

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
