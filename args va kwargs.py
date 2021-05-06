# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:22:28 2021

@author: LENOVO Y50-70
"""

#                         ' *args va **kwargs '



def summa(*sonlar):
    '''kiritilgan sonlar yigi'indisini hisoblaydigan funksiya'''
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2,))    
print(summa(2,3,4,5,6))
print(summa(1,3,5))
        
              " sum "
         
def summa(*sonlar):
    '''kiritilgan sonlar yigi'indisini hisoblaydigan funksiya''' 
    return sum(sonlar)
print(summa(1,2,))    
print(summa(2,3,4,5,6))
print(summa(1,3,5))

def summa(x,y,*sonlar):
   '''kiritilgan sonlar yigi'indisini hisoblaydigan funksiya''' 
    return x+y+sum(sonlar)

print(summa(1,2))
print(summa(2,3,6,4))
print(summa(1,3,9,7,5))

def avto_info(kompaniya,model,**malumotlar):
   '''Avto haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya'''
   malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info("GM", 'Gentra', rang='qora', karobka='avtomat')
avto2 = avto_info("Toyota", 'Camry', rang='oq', karobka='mexanika', narx=43000)
print(avto1)
print(avto2)