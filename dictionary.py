# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:46:16 2021

@author: LENOVO Y50-70
"""

#                            "  DICTIONARY  "



car_0 ={'model':'spark', 'rang':'oq'}
print(car_0['model'])
print(car_0['rang'])     

en_uz = {'father':'ota', 'mother':'Ona', 'family':'oila'}
print(en_uz)
print(en_uz['family'])

meva = {'olma':5000, 'banan':21000, 'uzum':16000}
print(f"banan narxi {meva['banan']} so'm")

talaba_0 = {'ism':'anvar boynazarov', 'yosh':'30', 't_yil':'1990'}
print(f"{talaba_0['ism'].title()},\
      {talaba_0['t_yil']}-yilda tug'ulgan,\
      {talaba_0['yosh']}-yoshda")
talaba_0['kurs'] = 3
talaba_0['fakultet'] = 'jismoniy tarbiya'  
talaba_0['ism'] = 'Abdulloh'    

talaba1 = {}
talaba1['ism'] = 'jafar alimov'
talaba1['kurs'] = 3talaba1['yosh'] = 21
print(talaba1)

#             QIYMATNI YANGILASH


talaba1['kurs'] = 4
print(f"talaba: {talaba1['ism'].title()} {talaba1['kurs']}-kurs")

#             KALIT SO'ZNI O'CHIRISH 

del talaba_0['t_yil']

#   AMALIYOT

men = {'ism':'zahriddin', 'familiya':'abduvaliyev', 'yosh': 22}
print(f'mening ismim- {men["ism"].title()},\
      familiyam- {men["familiya"].title()},\
      yoshim- {men["yosh"]} da')
      
taom = []
taom = 'manti'
taom = "qozonkabob"
taom = 'osh'
taom = "sho'rva"   
taom = 'dimlama'

taomlar = {
    'ali':'osh',
    'vali':'chuchvara',
    "g'ani":'dimlama',
    'joka':'qozonkabob',
    'serikbay':'norin'
    }

taom = taomlar['joka']
print(f'Jokaning sevimli taomi {taom.upper()}')
