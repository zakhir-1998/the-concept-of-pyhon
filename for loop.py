# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:17:38 2021

@author: LENOVO Y50-70
"""

#                             "FOR LOOP"



mehmonlar = ['Ali', "Yahyo", 'Jahongir', "Fazliddin"]
for k in mehmonlar:
    print("hello", k)
    print("good bye", k)

mehmonlar = ["snake", "bear", "horse", "wolf"]
for w in mehmonlar:
   print(f"Hurmatli o'rmonimiz a'zosi {w}, sizni 16-Aprel kuni o'rmonga taklif qilamiz.")
   print("Hurmat bilan, Bo'rivoylar oilasi.\n")

sonlar = list(range(1,11))
sonlar_kvadrati = []
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
    
sonlar = list(range(11))    
sonlar_kvadrati = []
for son in sonlar:    
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)

juralar = []
print("5 ta eng yaqin jurangiz kim?")
for w in range(5):
   juralar.append(input(f"{w+1}- jurangizni ismini kiriting: "))
print(juralar)