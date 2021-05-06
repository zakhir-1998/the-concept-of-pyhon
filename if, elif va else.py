# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:23:38 2021

@author: LENOVO Y50-70
"""

#                          "IF - ELIF - ELSE



print("Assalomu alaykum.Hayvonot bog'imizga hush kelibsiz!")
yosh = int(input("Yoshingiz nechchida?:\n>>>"))
if yosh<=5:
    print("sizga kirish bepul!")
elif yosh<=12:
    print("sizga kirish 3000 sum")
else:
    print("sizga kirish 5000 sum")
   

kun = input("Bugun nima kun?\n>>>")
if kun.lower()== 'shanba' or  kun.lower()== 'yakshanba':
    print("Tog'ga dam olgani kettik.")
else:
    print("Afsuski,bugun ish kuni!")
    
kun = input("Bugun nima kun?\n>>>")
harorat = float(input("Havo harorati qanday?\n>>>"))
if kun.lower()== 'yakshanba' and harorat >=30:
   print("Havo anchagina issiq.Cho'milgani kettik!")
elif kun.lower()== 'yakshanba' and harorat <=30:
   print("Havo sal isigandan keyin cho'milishga boramiz!")   
else:
    print("Afsuski bugun ishlarimiz ko'p")
    
kun = input ("Bugun qanday kun?\n>>>")
harorat = float(input("Havo nechchi gradus?\n>>>"))
if (kun.lower()== 'yakshanba' or kun.lower()== 'shanba') and harorat>=25:
    print("Dam olishga kettik")
elif (kun.lower()== 'yakshanba' or kun.lower()== 'shanba') and harorat<25:
    print("Havo hali salqinroq ekan.Boshqa safar dam olamiz")
    
narx = 15000
choy = True
salat = True
if choy and salat:
    narx = narx + 6000
elif choy or salat:
    narx = narx + 5000
print(f"Jami {narx} sum")


narx = 20000
choy = 1
non = 1
kompot = 0
salat = 1
assarti = 0

if choy:
    print("Mijoz choy oldi")
if non:
    print("Mijoz non oldi")
    narx = narx + 3000 
if kompot:
    print("Mijoz kompot oldi")
    narx = narx + 5000
if salat:
    print("Mijoz salat oldi")
    narx = narx + 8000
if assarti:
    print("Mijoz assarti oldi")
    narx = narx + 15000
print(f"Jami: {narx} sum") 

menu = ['osh', 'shashlik', 'mastava', "grill", 'jo\'ja']
ovqat = input("nima ovqat yeysiz?\n>>>")
if ovqat.lower() in menu:
    print("Buyurtmangiz qabul qilindi!")

else:
    print("Afsuski so'ralgan ovqat menuda qolmagan")  
    
menu = ["osh", "chuchvara", "lag'mon", "tovuq"]
buyurtmalar = ["manti", "somsa", "osh", "tovuq"]
if buyurtmalar:
   for taom in buyurtmalar:
      if taom in menu:
        print(f"menuda {taom} bor!")
else:
        print(f"menuda {taom} yo'q")     
    
