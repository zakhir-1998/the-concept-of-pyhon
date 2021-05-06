# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:58:16 2021

@author: LENOVO Y50-70
"""

#                          "WHILE VA RO'YXATLAR"



print("Yaqin insonlaringiz ro'yxatini tuzamiz.")
ismlar = []
n=1
while True:
    savol = f'{n}-yaqin insonningizni  ismini kiriting:\n>>> '
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("yana ism qo'shasizmi? ('xa yoki yoq' ): ")
    n+=1
    if takrorlash != 'xa':
        break
    
print("Yaqinlaringiz ro'yxati: ")
for ism in ismlar:
    print(ism.title())
    
juralar = {}
ishora = True
while ishora :
    ism = input('Juralaringizni ismini kiriting: ')
    yosh = input(f'{ism.title()}ning yoshini kiriting: ')
    juralar[ism] = int(yosh)
    
    javob = input("yana ma'lumot qo'shasizmi? ('xa' yoki 'yoq'): ")
    if javob == "yoq":
        ishora = False
         
for ism, yosh in juralar.items():
    print(f"{ism.title()} {yosh} yoshda")

cars = ['lacetti', 'nexia', 'cobalt', 'lacetti', 'orlando']
car = 'lacetti'
while car in cars:
    cars.remove('lacetti')
    
print(cars)

talabalar = ['qodir', 'botir', 'sobir', 'shokir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi!")
    baholangan_talabalar = int(baho)