# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:53:21 2021

@author: LENOVO Y50-70
"""

#                                "NESTING"



car0 = {
        'model':'lacetti', 
        'rang':'oq',
        'uzatma':'mexanika',
        'yil':2010,
        'km':103000,
        'narx':8000
        }

car1 = {
        'model':'spark',
        'rang':'silver',
        'uzatma':'avtomat',
        'yil':2019,
        'km':18000,
        'narx':8200
        } 

car2 = {
        'model':'cobalt',
        'rang':'qora',
        'uzatma':'avtomat',
        'yil':2020,
        'km':3000,
        'narx':11000
        }

car = car0
print(f'{car["model"].title()}, '
      f'{car["rang"]} rang, '
      f'{car["yil"]}-yil, {car["uzatma"]}, '
      f'{car["narx"]}$')
car = car1
print(f'{car["model"].title()}, '
      f'{car["rang"]} rang, '
      f'{car["yil"]}-yil, {car["uzatma"]}, '
      f'{car["narx"]}$')
car = car2
print(f'{car["model"].title()}, '
      f'{car["rang"]} rang, '
      f'{car["yil"]}-yil, {car["uzatma"]}, '
      f'{car["narx"]}$')      
  
#  NESTING bilan hammasini birdaniga chiqarish 

cars = [car0, car1, car2,]
for car in cars:
      print(f'{car["model"].title()}, '
      f'{car["rang"]} rang, '
      f'{car["yil"]}-yil, {car["uzatma"]}, '
      f'{car["narx"]}$')
 
print(f'{cars[2]["rang"].title()} '
      f'{cars[2]["model"]}')      

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2021,
        'narx':None,
        'km':0,
        'uzatma':'avtomat'
        }
    malibus.append(new_car)
    
for malibu in malibus:
    print(malibu)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus:
    print(malibu)
for malibu in malibus[3:6]:
    malibu["rang"]='qora'
    malibu["uzatma"]='mexanika'
for malibu in malibus:
    print(malibu)
for malibu in malibus[6:]:
    malibu['rang']='gan'
    malibu['uzatma']='mexanika'
for malibu in malibus:
    print(malibu)
    
for malibu in malibus:
    if malibu['uzatma']=='avtomat':
        malibu['narx']=36000
    else:
        malibu['narx']=32000
for malibu in malibus:
    print(malibu)        
    
dasturchilar = {
    'ali':['python, c++'],
    'vali':['sql, c#'],
    "g'ani":['java, kotlin'],
    'anvar':['php, html']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
        
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til.upper()} ", end="")
       
hamkasblar = {
        'utkir':{'familiya':'suvonkulov',
                 'tyil':1983,
                 'malumoti':'oliy',
                 'tillar':['javascript', 'java']},
        'alisher':{'familiya':'azimov',
                  'tyil':1998,
                   'malumoti':"o'rta maxsus",
                   'tillar':['php, html']}
                   }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ulgan. "
          f"malumoti: {info['malumoti']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())