# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:51:02 2021

@author: LENOVO Y50-70
"""

#                     "  LUG'AT BILAN ISHLASH  "



talaba1 = {
    'ism':'alijon',
    'familiya':'keldiyev',
    'yosh': 23,
    'fakultet':'nano texnologiya',
    'kurs':'4'
    } 
print(talaba1.items()) 
for kalit, qiymat in talaba1.items():
    print(f'kalit:{kalit}')
    print(f'qiymat:{qiymat}\n')

telefon = {
    "ali":'galaxy a50',
    'vali':'note 9',
    "g'ani":'iphone 7',
    'dilshod':'mi 8 pro',
    'akrom':'iphone 7'
    }
for k, q in telefon.items():
    print(f'{k.title()}ning telefoni {q.title()}') 
    
mahsulotlar = {
    'olma': 6000,
    'anjir': 18000,
    'gilos': 8500,
    'o\'rik': 25000,
    }
print(mahsulotlar.keys())  
print("do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar:
    print(mahsulot.title())
    
bozorlik = ['anor', 'olma', 'banan', 'anjir']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f'iltimos, do\'koningizga {buyum} ham olib keling')
        
print("do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
   
print("foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefon.values():
    print(tel)
   
print("foydalanuvchilar quidagi telefonlarni ishlatishadi:")
for tel in set(telefon.values()):
    print(tel) 