# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:18:44 2021

@author: LENOVO Y50-70
"""

#                          "IF ELSE VA TARMOQLASH"



avtomobillar = ["audi", 'chevrolet', 'corvette', 'bentley', 'bmw']
for avtomobil in avtomobillar:
    if avtomobil == 'bmw':
      print(avtomobil.upper())
    else:
      print(avtomobil.title())
     
ism = "Nosir"
ism.lower() == "nosir"     

familiya = input('familiyangiz nima?\n>>> ')
if familiya.lower() != 'abdurahimov':
    print(f'Uzur, {familiya.title()} bizga Abdurahimov kerak.')
else:
    print("Salom, Abdurahimov. Sizni ko'rganimizdan hursandmiz.")

javob = float(input('5*5 nechchiga teng?>>>')) 
if javob!=25:
    print("javobingiz xato")
else:
   print("javobingiz to'g'ri") 
   
   yosh = int(input("Yoshingiz nechchida? >>> "))
if yosh>=18:
    print("Xush kelibsiz!")
else:
    print("Kirishingiz mumkin emas!")
    
login = input("Yangi login kiriting: ")    
if len(login)<=5:
    print("Login 5 harfdan kam bo'lmasligi lozim!")
else:
    print("loginingiz qabul qilindi.Operator javobini kuting.")
    
yil = int(input("Tug'ulgan yilingizni kiriting:"))
if 2021-yil<18:
   print(f"Yoshingiz {2021-yil} da ekan.")    
   print("Kirish mumkin emas!")
else:
    print("Jamoamizga xush kelibsiz!")
    
yosh = int(input("Yoshingizni kiriting:>>> "))  
if yosh>60: print("Sizning covid-19 ga chalinish ehtimolingiz yuqori!") 
else:
    print("Sizning covid-19 ga chalinish ehtimolingiz yuqori emas.O'zingizni extiyot qiling!")


davlat = input("Assalomu alaykum.Qaysi Davlatdan tashrif buyurdingiz: ")
if davlat.lower() != "o'zbekiston":
    print(f"Kechirasiz, {davlat.title()} fuqarolari uchun kirish mumkin emas!")
else:
    print("Hush kelibsiz!")   
    
    
    
davlat = input("Dunyodagi eng katta davlat qaysi?\n>>>>")
if davlat.lower() != 'rossiya':
    print("Javobingiz noto'g'ri!")
else:
    print(f"Albatta bu {davlat.upper()} edi.")
    print("yana bir bor o'zingizni sinab ko'ring!")