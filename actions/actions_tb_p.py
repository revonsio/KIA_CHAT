from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction

class ActionDataTinggibadanPria(Action):
    def name(self):
        return "action_data_tinggibadan_pria"

    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        umur = float(tracker.get_slot("umur"))
        tinggi_badan = float(tracker.get_slot("tinggi_badan"))
            
        if umur == 0:
            median = 49.9
            if tinggi_badan < median:
                nsbr = 48
            elif tinggi_badan > median:
                nsbr = 51.8
            else:
                nsbr = median
        elif umur == 1:
            median = 54.7
            if tinggi_badan < median:
                nsbr = 52.8
            elif tinggi_badan > median:
                nsbr = 56.7
            else:
                nsbr = median
        elif umur == 2:
            median = 58.4
            if tinggi_badan < median:
                nsbr = 56.4
            elif tinggi_badan > median:
                nsbr = 60.4
            else:
                nsbr = median
        elif umur == 3:
            median = 61.4
            if tinggi_badan < median:
                nsbr = 59.4
            elif tinggi_badan > median:
                nsbr = 63.5
            else:
                nsbr = median
        elif umur == 4:
            median = 63.9
            if tinggi_badan < median:
                nsbr = 61.8
            elif tinggi_badan > median:
                nsbr = 66
            else:
                nsbr = median
        elif umur == 5:
            median = 65.9
            if tinggi_badan < median:
                nsbr = 63.8
            elif tinggi_badan > median:
                nsbr = 68
            else:
                nsbr = median
        elif umur == 6:
            median = 67.6
            if tinggi_badan < median:
                nsbr = 65.5
            elif tinggi_badan > median:
                nsbr = 69.8
            else:
                nsbr = median
        elif umur == 7:
            median = 69.2
            if tinggi_badan < median:
                nsbr = 67
            elif tinggi_badan > median:
                nsbr = 71.3
            else:
                nsbr = median
        elif umur == 8:
            median = 70.6
            if tinggi_badan < median:
                nsbr = 68.4
            elif tinggi_badan > median:
                nsbr = 72.8
            else:
                nsbr = median
        elif umur == 9:
            median = 72
            if tinggi_badan < median:
                nsbr = 69.7
            elif tinggi_badan > median:
                nsbr = 74.2
            else:
                nsbr = median
        elif umur == 10:
            median = 73.3
            if tinggi_badan < median:
                nsbr = 71
            elif tinggi_badan > median:
                nsbr = 75.6
            else:
                nsbr = median
        elif umur == 11:
            median = 74.5
            if tinggi_badan < median:
                nsbr = 72.2
            elif tinggi_badan > median:
                nsbr = 76.9
            else:
                nsbr = median
        elif umur == 12:
            median = 75.7
            if tinggi_badan < median:
                nsbr = 73.4
            elif tinggi_badan > median:
                nsbr = 78.1
            else:
                nsbr = median
        elif umur == 13:
            median = 76.9
            if tinggi_badan < median:
                nsbr = 74.5
            elif tinggi_badan > median:
                nsbr = 79.3
            else:
                nsbr = median
        elif umur == 14:
            median = 78
            if tinggi_badan < median:
                nsbr = 75.6
            elif tinggi_badan > median:
                nsbr = 80.5
            else:
                nsbr = median
        elif umur == 15:
            median = 79.1
            if tinggi_badan < median:
                nsbr = 76.6
            elif tinggi_badan > median:
                nsbr = 81.7
            else:
                nsbr = median
        elif umur == 16:
            median = 80.2
            if tinggi_badan < median:
                nsbr = 77.6
            elif tinggi_badan > median:
                nsbr = 82.8
            else:
                nsbr = median
        elif umur == 17:
            median = 81.2
            if tinggi_badan < median:
                nsbr = 78.6
            elif tinggi_badan > median:
                nsbr = 83.9
            else:
                nsbr = median
        elif umur == 18:
            median = 82.3
            if tinggi_badan < median:
                nsbr = 79.6
            elif tinggi_badan > median:
                nsbr = 85
            else:
                nsbr = median
        elif umur == 19:
            median = 83.2
            if tinggi_badan < median:
                nsbr = 80.5
            elif tinggi_badan > median:
                nsbr = 86
            else:
                nsbr = median
        elif umur == 20:
            median = 84.2
            if tinggi_badan < median:
                nsbr = 81.4
            elif tinggi_badan > median:
                nsbr = 87
            else:
                nsbr = median
        elif umur == 21:
            median = 85.1
            if tinggi_badan < median:
                nsbr = 82.3
            elif tinggi_badan > median:
                nsbr = 88
            else:
                nsbr = median
        elif umur == 22:
            median = 86
            if tinggi_badan < median:
                nsbr = 83.1
            elif tinggi_badan > median:
                nsbr = 89
            else:
                nsbr = median
        elif umur == 23:
            median = 86.9
            if tinggi_badan < median:
                nsbr = 83.9
            elif tinggi_badan > median:
                nsbr = 89.9
            else:
                nsbr = median
        elif umur == 24:
            median = 87.8
            if tinggi_badan < median:
                nsbr = 84.8
            elif tinggi_badan > median:
                nsbr = 90.9
            else:
                nsbr = median
        elif umur == 25:
            median = 88
            if tinggi_badan < median:
                nsbr = 84.9
            elif tinggi_badan > median:
                nsbr = 91.1
            else:
                nsbr = median
        elif umur == 26:
            median = 88.8
            if tinggi_badan < median:
                nsbr = 85.6
            elif tinggi_badan > median:
                nsbr = 92
            else:
                nsbr = median
        elif umur == 27:
            median = 89.6
            if tinggi_badan < median:
                nsbr = 86.4
            elif tinggi_badan > median:
                nsbr = 92.9
            else:
                nsbr = median
        elif umur == 28:
            median = 90.4
            if tinggi_badan < median:
                nsbr = 87.1
            elif tinggi_badan > median:
                nsbr = 93.7
            else:
                nsbr = median
        elif umur == 29:
            median = 91.2
            if tinggi_badan < median:
                nsbr = 87.8
            elif tinggi_badan > median:
                nsbr = 94.5
            else:
                nsbr = median
        elif umur == 30:
            median = 91.9
            if tinggi_badan < median:
                nsbr = 88.5
            elif tinggi_badan > median:
                nsbr = 95.3
            else:
                nsbr = median
        elif umur == 31:
            median = 92.7
            if tinggi_badan < median:
                nsbr = 89.2
            elif tinggi_badan > median:
                nsbr = 96.1
            else:
                nsbr = median
        elif umur == 32:
            median = 93.4
            if tinggi_badan < median:
                nsbr = 89.9
            elif tinggi_badan > median:
                nsbr = 96.9
            else:
                nsbr = median
        elif umur == 33:
            median = 94.1
            if tinggi_badan < median:
                nsbr = 90.5
            elif tinggi_badan > median:
                nsbr = 97.6
            else:
                nsbr = median
        elif umur == 34:
            median = 94.8
            if tinggi_badan < median:
                nsbr = 91.1
            elif tinggi_badan > median:
                nsbr = 98.4
            else:
                nsbr = median
        elif umur == 35:
            median = 95.4
            if tinggi_badan < median:
                nsbr = 91.8
            elif tinggi_badan > median:
                nsbr = 99.1
            else:
                nsbr = median
        elif umur == 36:
            median = 96.1
            if tinggi_badan < median:
                nsbr = 92.4
            elif tinggi_badan > median:
                nsbr = 99.8
            else:
                nsbr = median
        elif umur == 37:
            median = 96.7
            if tinggi_badan < median:
                nsbr = 93
            elif tinggi_badan > median:
                nsbr = 100.5
            else:
                nsbr = median
        elif umur == 38:
            median = 97.4
            if tinggi_badan < median:
                nsbr = 93.6
            elif tinggi_badan > median:
                nsbr = 101.2
            else:
                nsbr = median
        elif umur == 39:
            median = 98
            if tinggi_badan < median:
                nsbr = 94.2
            elif tinggi_badan > median:
                nsbr = 101.8
            else:
                nsbr = median
        elif umur == 40:
            median = 98.6
            if tinggi_badan < median:
                nsbr = 94.7
            elif tinggi_badan > median:
                nsbr = 102.5
            else:
                nsbr = median
        elif umur == 41:
            median = 99.2
            if tinggi_badan < median:
                nsbr = 95.3
            elif tinggi_badan > median:
                nsbr = 103.2
            else:
                nsbr = median
        elif umur == 42:
            median = 99.9
            if tinggi_badan < median:
                nsbr = 95.9
            elif tinggi_badan > median:
                nsbr = 103.8
            else:
                nsbr = median
        elif umur == 43:
            median = 100.4
            if tinggi_badan < median:
                nsbr = 96.4
            elif tinggi_badan > median:
                nsbr = 104.5
            else:
                nsbr = median
        elif umur == 44:
            median = 101
            if tinggi_badan < median:
                nsbr = 97
            elif tinggi_badan > median:
                nsbr = 105.1
            else:
                nsbr = median
        elif umur == 45:
            median = 101.6
            if tinggi_badan < median:
                nsbr = 97.5
            elif tinggi_badan > median:
                nsbr = 105.7
            else:
                nsbr = median
        elif umur == 46:
            median = 102.2
            if tinggi_badan < median:
                nsbr = 98.1
            elif tinggi_badan > median:
                nsbr = 106.3
            else:
                nsbr = median
        elif umur == 47:
            median = 102.8
            if tinggi_badan < median:
                nsbr = 98.6
            elif tinggi_badan > median:
                nsbr = 106.9
            else:
                nsbr = median
        elif umur == 48:
            median = 103.3
            if tinggi_badan < median:
                nsbr = 99.1
            elif tinggi_badan > median:
                nsbr = 107.5
            else:
                nsbr = median
        elif umur == 49:
            median = 103.9
            if tinggi_badan < median:
                nsbr = 99.7
            elif tinggi_badan > median:
                nsbr = 108.1
            else:
                nsbr = median
        elif umur == 50:
            median = 104.4
            if tinggi_badan < median:
                nsbr = 100.2
            elif tinggi_badan > median:
                nsbr = 108.7
            else:
                nsbr = median
        elif umur == 51:
            median = 105
            if tinggi_badan < median:
                nsbr = 100.7
            elif tinggi_badan > median:
                nsbr = 109.3
            else:
                nsbr = median
        elif umur == 52:
            median = 105.6
            if tinggi_badan < median:
                nsbr = 101.2
            elif tinggi_badan > median:
                nsbr = 109.9
            else:
                nsbr = median
        elif umur == 53:
            median = 106.1
            if tinggi_badan < median:
                nsbr = 101.7
            elif tinggi_badan > median:
                nsbr = 110.5
            else:
                nsbr = median
        elif umur == 54:
            median = 106.7
            if tinggi_badan < median:
                nsbr = 102.3
            elif tinggi_badan > median:
                nsbr = 111.1
            else:
                nsbr = median
        elif umur == 55:
            median = 107.2
            if tinggi_badan < median:
                nsbr = 102.8
            elif tinggi_badan > median:
                nsbr = 111.7
            else:
                nsbr = median
        elif umur == 56:
            median = 107.8
            if tinggi_badan < median:
                nsbr = 103.3
            elif tinggi_badan > median:
                nsbr = 112.3
            else:
                nsbr = median
        elif umur == 57:
            median = 108.3
            if tinggi_badan < median:
                nsbr = 103.8
            elif tinggi_badan > median:
                nsbr = 112.8
            else:
                nsbr = median
        elif umur == 58:
            median = 108.9
            if tinggi_badan < median:
                nsbr = 104.3
            elif tinggi_badan > median:
                nsbr = 113.4
            else:
                nsbr = median
        elif umur == 59:
            median = 109.4
            if tinggi_badan < median:
                nsbr = 104.8
            elif tinggi_badan > median:
                nsbr = 114
            else:
                nsbr = median
        elif umur == 60:
            median = 110
            if tinggi_badan < median:
                nsbr = 105.3
            elif tinggi_badan > median:
                nsbr = 114.6
            else:
                nsbr = median
        else:
            dispatcher.utter_message(text="Data yang Anda masukkan tidak valid (Error: Umur harus tidak lebih  dari 60 bulan).")

        if tinggi_badan < median:
            zscore = (tinggi_badan - median) / (median - nsbr)
        else:
            zscore = (tinggi_badan - median) / (nsbr - median)

        dispatcher.utter_message(text="Data berat badan anak Anda: \n 1. Jenis Kelamin: Laki-laki \n 2. Umur: " + str(umur) + " bulan" + "\n" "3. Tinggi Badan:" + str(tinggi_badan) + " cm")

        if zscore < -3:
            dispatcher.utter_message(text="Kategori: Sangat pendek (severely stunted)\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore >= -3 and zscore <= -2:
            dispatcher.utter_message(text="Kategori: Pendek (stunted)\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore > -2 and zscore <= 3:
            dispatcher.utter_message(text="Kategori: Normal\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")
        elif zscore > 3:
            dispatcher.utter_message(text="Kategori: Tinggi\n Sumber: Permenkes No. 2 Tahun 2020 Tentang Standar Antropometri Anak")

        if umur > 0 and umur <= 24:
            dispatcher.utter_message(image="https://i.ibb.co/FH5fbHb/image.png")
        else:
            dispatcher.utter_message(image="https://i.ibb.co/5RWgfjS/image.png")
        
        return []