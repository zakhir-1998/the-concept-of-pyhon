# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:01:58 2021

@author: LENOVO Y50-70
"""

#                       'FUNCTIONS' (FUNKTSIYALAR)

 
def salom_ber():
            """salom beruvchi funksiya"""
        print("Assalomu alaykum!")
    
salom_ber()    

def salom_ber(ism):
        '''foydalanuvchini ismini qabul qilib 
    unga salom beradigan funksiya'''
    print(f"Assalomu alaykum, hurmatli {ism.title()}")
    
salom_ber("abdunasim")
salom_ber("nargiza")

def toliq_ism(ism, familiya):
    """foydalnuvchini ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"foydalanuvchi ismi: {ism.title()}\n"
          f'foydalanuvchi familiyasi: {familiya.title()}')
    
toliq_ism('olim' , 'hakimov')

def yosh_hisobla(t_yil, xozirgi_yil=2021):
    """foydlanuvchining yoshini hisoblaydi"""
    print(f"siz {t_yil-xozirgi_yil} yoshdasiz")
    
yosh_hisobla(1995)

def pul_sana(oylik_daromad):
   """foydalnuvchini oylik daromadini hisoblaydi"""
    print(f"siz yiliga {oylik_daromad}mln miqdorda daromad ko'rasiz")
    

pul_sana(2)    