# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:44:36 2021

@author: LENOVO Y50-70
"""

#                     SyntaxError   (SINTAKSIS XATOLAR)
 

print "hello world"   #"print" dan keyin qovus () ochiladi
print ("hello world"  #'unexpected EOF while parsing' funksiyani yopishda xato qilinsa chiqadi 
                       #"EOL while scanning scring literal"- bunda qatorni yakunida xatolik bor degani

son = input("istlgan sonni kiriting\n>>>")  
son = int(son)                
print(f"{son} ning kvadrati {son**2} ga teng!")   

mevalar = ["olma", "anor", "gilos"]
for meva in mevalar:
    print(meva)
    
son = int(input("istalgan sonni kiriting\n>>>"))
ildiz = son**(1/2)  
print(f"{son} ning ildizi {ildiz} ga teng")