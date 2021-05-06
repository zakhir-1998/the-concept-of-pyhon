# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:21:36 2021

@author: LENOVO Y50-70
"""

#                       'FUNKSIYAGA RO'YXAT UZATISH'



def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar

talabalar = ['ali', 'vali', 'nozim', 'sobir']
baholar = bahola(talabalar[:])
print(baholar)