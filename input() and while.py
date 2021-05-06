# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:56:25 2021

@author: LENOVO Y50-70
"""

#                           ' INPUT() VA WHILE '



ism = input('ismingizni kiriting?\n>>> ')
savol = f"Salom, {ism.title()}.Yoshingiz nechchida?\n>>> "
yosh = input(savol)
yosh = int(yosh)
height = input("Bo'yingiz uzunligi qancha?\n>>> ")
height = float(height)

son = 1
while son<=10:
    print(son, end= '')
    son += 1   # yoki (son = son + 1)

print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
savol = 'istalgan son kiriting '
savol += "(Dasturni to'xtatish uchun 'close' deb yozing!): "
qiymat = ''
while qiymat != 'close':
    qiymat = input(savol)
    if qiymat != 'close':
        print(float(qiymat)**2)
print('Jarayon yakunlandi.')        
    
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print('dastur tugadi')

while True:
    qiymat = input(savol)
    if qiymat == 'close':
        break
    else:
        print(float(qiymat)**2)
print('dastur tugadi')

 CONTINUE
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng!")
    
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng!")
 
son = 1 
while son>0:
    son = son + 1
    if son%2!=0:
        continue
    else:
        print(son)