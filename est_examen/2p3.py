# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:54:09 2022

@author: JHOSS
"""

def contrarPalabras(palabras):
    contadorPalabras = 0
    palabrasList = []
    palabra=''
    index = 0
    for character in palabras:
           
        
        if character == ' ':
            palabrasList.append(palabra)
            # reinicializamos todo
            palabra=''
        else:
            palabra += character
        
        # final del array de caracteres
        if index + 1 == len(palabrasList) :
            palabrasList.append(palabra)
            
    return len(palabrasList)

print (contrarPalabras('Hola Mundo hola hola')) #retorna 4