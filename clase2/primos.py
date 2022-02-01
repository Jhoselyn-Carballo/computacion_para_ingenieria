# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 09:38:18 2022

@author: JHOSS
"""

#CONTAR LOS NUMEROS PRIMOS DEL 1 AL 100
num = 1
while num <=100:
    cont =1
    x=0
    while cont <= num:
        if num % cont == 0:
            x=x+1
        cont = cont +1
    if x==2:
        print(num)
    num = num +1
    
        
     
    