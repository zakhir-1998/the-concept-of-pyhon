# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:04:09 2021

@author: LENOVO Y50-70
"""

#                         'FUNKSIYADAN QIYMAT QAYTARISH'



def toliq_ism_yasa(ism, familiya):
    '''toliq ism qaytaruvchi funksiya'''
    toliq_ism = f"{ism.title()} {familiya.title()}"
    return toliq_ism 
    
talaba1 = toliq_ism_yasa('abdunasim', 'abdurahimov')
talaba2 = toliq_ism_yasa('nargiza', 'abdurahimova')
print(f'{talaba1} darsga kechikib keldi, {talaba2} esa darsga kelmadi')

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    '''toliq ism qaytaruvchi funksiya'''
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f'{ism} {familiya}'
    return toliq_ism.title()    
    
talaba1 = toliq_ism_yasa('fazliddin', 'abduvaliyev')
talaba2 = toliq_ism_yasa('laziza', 'nazarova', 'abdunasim qizi')
print(f"sinfimiz a'lochilari: {talaba1}, {talaba2}")

 
  avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'karobka':karobka,
        'yil':yili,
        'narx':narxi}
   return avto

avto1 = avto_info('GM', 'malibu', 'qora', 'avtomat', 2019)
avto2 = avto_info('BMW', 'X6', 'oq', 'mexanika', 2020, 75000)
avtolar = [avto1, avto2]
print('onlayn bozordagi mavjud avtomoshinalar:')
for avto in avtolar:
    if avto['narx']:
          narx = avto['narx']
    else:
        narx = "No'malum"
    print(f"{avto['rang']} {avto['kompaniya']} {avto['model']}. narxi: {narx}") 
    

def oraliq(min,max):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0,10))
print(oraliq(10,21))
    
def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'karobka':karobka,
        'yil':yili,
        'narx':narxi}
    return avto
print("saytimizdagi avtomashinalar ro'xatini tuzamiz.")
avtomashinalar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end="")
    kompaniya=input('ishlab chiqaruvchi: ')
    model=input("modeli: ")
    rang=input("rangi: ")
    karobka=input("korobka: ")
    yili=input("ishlab chiqarilgan yili: ")
    narxi=input("narxi: ")
    
    avtomashinalar.append(avto_info(kompaniya, model, rang, karobka, yili, narxi))
    javob = input("Yana avto qo'shasizmi? ('xa'yoki'yoq'): ")
    if javob=='yoq':
        break
    print("salonimizdagi avtomashinalar:")
    for avto in avtomashinalar:
        if avto['narx']:
            narx = avto['narx']
        else:
            narx = "No'malum"
print(f"{avto['rang'].title()} {avto['model'].title()} {karobka} karobka. narxi {narx}")    
            