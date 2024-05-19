from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction

class ActionDataTinggibadanWanita(Action):
    def name(self):
        return "action_data_tinggibadan_wanita"

    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        umur = float(tracker.get_slot("umur"))
        tinggi_badan = float(tracker.get_slot("tinggi_badan"))
            
        if umur == 0:
            median = 49.1
            if tinggi_badan < median:
                nsbr = 47.3
            elif tinggi_badan > median:
                nsbr = 51
            else:
                nsbr = median
        elif umur == 1:
            median = 53.7
            if tinggi_badan < median:
                nsbr = 51.7
            elif tinggi_badan > median:
                nsbr = 55.6
            else:
                nsbr = median
        elif umur == 2:
            median = 57.1
            if tinggi_badan < median:
                nsbr = 55
            elif tinggi_badan > median:
                nsbr = 59.1
            else:
                nsbr = median
        elif umur == 3:
            median = 59.8
            if tinggi_badan < median:
                nsbr = 57.7
            elif tinggi_badan > median:
                nsbr = 61.9
            else:
                nsbr = median
        elif umur == 4:
            median = 62.1
            if tinggi_badan < median:
                nsbr = 59.9
            elif tinggi_badan > median:
                nsbr = 64.3
            else:
                nsbr = median
        elif umur == 5:
            median = 64
            if tinggi_badan < median:
                nsbr = 61.8
            elif tinggi_badan > median:
                nsbr = 66.2
            else:
                nsbr = median
        elif umur == 6:
            median = 65.7
            if tinggi_badan < median:
                nsbr = 63.5
            elif tinggi_badan > median:
                nsbr = 68
            else:
                nsbr = median
        elif umur == 7:
            median = 67.3
            if tinggi_badan < median:
                nsbr = 65
            elif tinggi_badan > median:
                nsbr = 69.6
            else:
                nsbr = median
        elif umur == 8:
            median = 68.7
            if tinggi_badan < median:
                nsbr = 66.4
            elif tinggi_badan > median:
                nsbr = 71.1
            else:
                nsbr = median
        elif umur == 9:
            median = 70.1
            if tinggi_badan < median:
                nsbr = 67.7
            elif tinggi_badan > median:
                nsbr = 72.6
            else:
                nsbr = median
        elif umur == 10:
            median = 71.5
            if tinggi_badan < median:
                nsbr = 69
            elif tinggi_badan > median:
                nsbr = 73.9
            else:
                nsbr = median
        elif umur == 11:
            median = 72.8
            if tinggi_badan < median:
                nsbr = 70.3
            elif tinggi_badan > median:
                nsbr = 75.3
            else:
                nsbr = median
        elif umur == 12:
            median = 74
            if tinggi_badan < median:
                nsbr = 71.4
            elif tinggi_badan > median:
                nsbr = 76.6
            else:
                nsbr = median
        elif umur == 13:
            median = 75.2
            if tinggi_badan < median:
                nsbr = 72.6
            elif tinggi_badan > median:
                nsbr = 77.8
            else:
                nsbr = median
        elif umur == 14:
            median = 76.4
            if tinggi_badan < median:
                nsbr = 73.7
            elif tinggi_badan > median:
                nsbr = 79.1
            else:
                nsbr = median
        elif umur == 15:
            median = 77.5
            if tinggi_badan < median:
                nsbr = 74.8
            elif tinggi_badan > median:
                nsbr = 80.2
            else:
                nsbr = median
        elif umur == 16:
            median = 78.6
            if tinggi_badan < median:
                nsbr = 75.8
            elif tinggi_badan > median:
                nsbr = 81.4
            else:
                nsbr = median
        elif umur == 17:
            median = 79.7
            if tinggi_badan < median:
                nsbr = 76.8
            elif tinggi_badan > median:
                nsbr = 82.5
            else:
                nsbr = median
        elif umur == 18:
            median = 80.7
            if tinggi_badan < median:
                nsbr = 77.8
            elif tinggi_badan > median:
                nsbr = 83.6
            else:
                nsbr = median
        elif umur == 19:
            median = 81.7
            if tinggi_badan < median:
                nsbr = 78.8
            elif tinggi_badan > median:
                nsbr = 84.7
            else:
                nsbr = median
        elif umur == 20:
            median = 82.7
            if tinggi_badan < median:
                nsbr = 79.7
            elif tinggi_badan > median:
                nsbr = 85.7
            else:
                nsbr = median
        elif umur == 21:
            median = 83.7
            if tinggi_badan < median:
                nsbr = 80.6
            elif tinggi_badan > median:
                nsbr = 86.7
            else:
                nsbr = median
        elif umur == 22:
            median = 84.6
            if tinggi_badan < median:
                nsbr = 81.5
            elif tinggi_badan > median:
                nsbr = 87.7
            else:
                nsbr = median
        elif umur == 23:
            median = 85.5
            if tinggi_badan < median:
                nsbr = 82.3
            elif tinggi_badan > median:
                nsbr = 88.7
            else:
                nsbr = median
        elif umur == 24:
            median = 85.7
            if tinggi_badan < median:
                nsbr = 82.5
            elif tinggi_badan > median:
                nsbr = 88.9
            else:
                nsbr = median
        elif umur == 25:
            median = 86.6
            if tinggi_badan < median:
                nsbr = 83.3
            elif tinggi_badan > median:
                nsbr = 89.9
            else:
                nsbr = median
        elif umur == 26:
            median = 87.4
            if tinggi_badan < median:
                nsbr = 84.1
            elif tinggi_badan > median:
                nsbr = 90.8
            else:
                nsbr = median
        elif umur == 27:
            median = 88.3
            if tinggi_badan < median:
                nsbr = 84.9
            elif tinggi_badan > median:
                nsbr = 91.7
            else:
                nsbr = median
        elif umur == 28:
            median = 89.1
            if tinggi_badan < median:
                nsbr = 85.7
            elif tinggi_badan > median:
                nsbr = 92.5
            else:
                nsbr = median
        elif umur == 29:
            median = 89.9
            if tinggi_badan < median:
                nsbr = 86.4
            elif tinggi_badan > median:
                nsbr = 93.4
            else:
                nsbr = median
        elif umur == 30:
            median = 90.7
            if tinggi_badan < median:
                nsbr = 87.1
            elif tinggi_badan > median:
                nsbr = 94.2
            else:
                nsbr = median
        elif umur == 31:
            median = 91.4
            if tinggi_badan < median:
                nsbr = 87.9
            elif tinggi_badan > median:
                nsbr = 95
            else:
                nsbr = median
        elif umur == 32:
            median = 92.2
            if tinggi_badan < median:
                nsbr = 88.6
            elif tinggi_badan > median:
                nsbr = 95.8
            else:
                nsbr = median
        elif umur == 33:
            median = 92.9
            if tinggi_badan < median:
                nsbr = 89.3
            elif tinggi_badan > median:
                nsbr = 96.6
            else:
                nsbr = median
        elif umur == 34:
            median = 93.6
            if tinggi_badan < median:
                nsbr = 89.9
            elif tinggi_badan > median:
                nsbr = 97.4
            else:
                nsbr = median
        elif umur == 35:
            median = 94.4
            if tinggi_badan < median:
                nsbr = 90.6
            elif tinggi_badan > median:
                nsbr = 98.1
            else:
                nsbr = median
        elif umur == 36:
            median = 95.1
            if tinggi_badan < median:
                nsbr = 91.2
            elif tinggi_badan > median:
                nsbr = 98.9
            else:
                nsbr = median
        elif umur == 37:
            median = 95.7
            if tinggi_badan < median:
                nsbr = 91.9
            elif tinggi_badan > median:
                nsbr = 99.6
            else:
                nsbr = median
        elif umur == 38:
            median = 96.4
            if tinggi_badan < median:
                nsbr = 92.5
            elif tinggi_badan > median:
                nsbr = 100.3
            else:
                nsbr = median
        elif umur == 39:
            median = 97.1
            if tinggi_badan < median:
                nsbr = 93.1
            elif tinggi_badan > median:
                nsbr = 101
            else:
                nsbr = median
        elif umur == 40:
            median = 97.7
            if tinggi_badan < median:
                nsbr = 93.8
            elif tinggi_badan > median:
                nsbr = 101.7
            else:
                nsbr = median
        elif umur == 41:
            median = 98.4
            if tinggi_badan < median:
                nsbr = 94.4
            elif tinggi_badan > median:
                nsbr = 102.4
            else:
                nsbr = median
        elif umur == 42:
            median = 99
            if tinggi_badan < median:
                nsbr = 95
            elif tinggi_badan > median:
                nsbr = 103.1
            else:
                nsbr = median
        elif umur == 43:
            median = 99.7
            if tinggi_badan < median:
                nsbr = 95.6
            elif tinggi_badan > median:
                nsbr = 103.8
            else:
                nsbr = median
        elif umur == 44:
            median = 100.3
            if tinggi_badan < median:
                nsbr = 96.2
            elif tinggi_badan > median:
                nsbr = 104.5
            else:
                nsbr = median
        elif umur == 45:
            median = 100.9
            if tinggi_badan < median:
                nsbr = 96.7
            elif tinggi_badan > median:
                nsbr = 105.1
            else:
                nsbr = median
        elif umur == 46:
            median = 101.5
            if tinggi_badan < median:
                nsbr = 97.3
            elif tinggi_badan > median:
                nsbr = 105.8
            else:
                nsbr = median
        elif umur == 47:
            median = 102.1
            if tinggi_badan < median:
                nsbr = 97.9
            elif tinggi_badan > median:
                nsbr = 106.4
            else:
                nsbr = median
        elif umur == 48:
            median = 102.7
            if tinggi_badan < median:
                nsbr = 98.4
            elif tinggi_badan > median:
                nsbr = 107
            else:
                nsbr = median
        elif umur == 49:
            median = 103.3
            if tinggi_badan < median:
                nsbr = 99
            elif tinggi_badan > median:
                nsbr = 107.7
            else:
                nsbr = median
        elif umur == 50:
            median = 103.9
            if tinggi_badan < median:
                nsbr = 99.5
            elif tinggi_badan > median:
                nsbr = 108.3
            else:
                nsbr = median
        elif umur == 51:
            median = 104.5
            if tinggi_badan < median:
                nsbr = 100.1
            elif tinggi_badan > median:
                nsbr = 108.9
            else:
                nsbr = median
        elif umur == 52:
            median = 105
            if tinggi_badan < median:
                nsbr = 100.6
            elif tinggi_badan > median:
                nsbr = 109.5
            else:
                nsbr = median
        elif umur == 53:
            median = 105.6
            if tinggi_badan < median:
                nsbr = 101.1
            elif tinggi_badan > median:
                nsbr = 110.1
            else:
                nsbr = median
        elif umur == 54:
            median = 106.2
            if tinggi_badan < median:
                nsbr = 101.6
            elif tinggi_badan > median:
                nsbr = 110.7
            else:
                nsbr = median
        elif umur == 55:
            median = 106.7
            if tinggi_badan < median:
                nsbr = 102.2
            elif tinggi_badan > median:
                nsbr = 111.3
            else:
                nsbr = median
        elif umur == 56:
            median = 107.3
            if tinggi_badan < median:
                nsbr = 102.7
            elif tinggi_badan > median:
                nsbr = 111.9
            else:
                nsbr = median
        elif umur == 57:
            median = 107.8
            if tinggi_badan < median:
                nsbr = 103.2
            elif tinggi_badan > median:
                nsbr = 112.5
            else:
                nsbr = median
        elif umur == 58:
            median = 108.4
            if tinggi_badan < median:
                nsbr = 103.7
            elif tinggi_badan > median:
                nsbr = 113
            else:
                nsbr = median
        elif umur == 59:
            median = 108.9
            if tinggi_badan < median:
                nsbr = 104.2
            elif tinggi_badan > median:
                nsbr = 113.6
            else:
                nsbr = median
        elif umur == 60:
            median = 109.4
            if tinggi_badan < median:
                nsbr = 104.7
            elif tinggi_badan > median:
                nsbr = 114.2
            else:
                nsbr = median
        else:
            dispatcher.utter_message(text="Data yang Anda masukkan tidak valid (Error: Umur harus tidak lebih  dari 60 bulan).")

        if tinggi_badan < median:
            zscore = (tinggi_badan - median) / (median - nsbr)
        else:
            zscore = (tinggi_badan - median) / (nsbr - median)

        dispatcher.utter_message(text="Data berat badan anak Anda: \n 1. Jenis Kelamin: Perempuan \n 2. Umur: " + str(umur) + " bulan" + "\n" "3. Tinggi Badan:" + str(tinggi_badan) + " cm")

        if zscore < -3:
            dispatcher.utter_message(text="Kategori: Sangat pendek (severely stunted)\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore >= -3 and zscore <= -2:
            dispatcher.utter_message(text="Kategori: Pendek (stunted)\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore > -2 and zscore <= 3:
            dispatcher.utter_message(text="Kategori: Normal\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore > 3:
            dispatcher.utter_message(text="Kategori: Tinggi\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")

        if umur > 0 and umur <= 24:
            dispatcher.utter_message(image="https://i.ibb.co/VD3cgVJ/image.png")
        else:
            dispatcher.utter_message(image="https://i.ibb.co/z5bm3S9/image.png")            

        return []