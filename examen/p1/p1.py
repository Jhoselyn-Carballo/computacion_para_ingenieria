# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:10:48 2022

@author: JHOSS
"""

#Dada una cadena verificar que sea palindroma(es aquella palabra que se lee lo mismo al derecho y al reves e.j Ana)

#invertir un nombre

def invertirNombre(nombre):
    nombreInvertido=0
    while nombre > 0:
        nombreInvertido= 10 * nombreInvertido + nombre %10
        nombre//=10
    return nombreInvertido

entrada = int(input("ingrese la palabra:"))
nomInv = invertirNombre(entrada)
if entrada == nomInv:
    print("el nombre es palindromo")
else:
    print("el nombre no es palindromo")


