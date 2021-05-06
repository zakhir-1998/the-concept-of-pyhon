# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:12:58 2021

@author: LENOVO Y50-70
"""

#                             "List"



mevalar = ['olma', 'anor', 'banan', 'kivi' ]
narxlar = ['5600', '18000', '15000', '35000']
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []

bozorlik = ["yog'", 'un', "go'sht", 'piyoz', 'karam']
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot +" sotib oldim")
print("olinmagan mahsulotlar ro'yxati: ", bozorlik)

p = ["Moshina", "Uy", "Mototsikl", "Arava"]
w = p.pop(0)
print("Men " + w + " olishga erishdim")
print("Hali ololmaganlarim esa: ", p)

# .append() - RO'YXATGA YANGI ELEMENT QO'SHISH (HAR DOIM RO'YXATNI OXIRIGA QO'SHADI)
# .insert() - RO'YXATNING BOSHIGA,O'RTASIGA VA OXIRIGA ELEMENT QO'SHISH (RO'YXATNI BOSHI YOKI OXIRIGA ELEMENT QO'SHMOQCHI BO'LSAK .insert DAN KEYIN ( ) TARZDA 'INDEX' YOZILADI)
