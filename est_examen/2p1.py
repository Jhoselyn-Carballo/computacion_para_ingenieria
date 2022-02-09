# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:47:27 2022

@author: JHOSS
"""

entrada = input ("ingrese una frase:")
contador = 0
for char in entrada:
    
    if char == ' ':
        contador+=1
print("el contador es el siguiente--->", contador)