# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:10:48 2022

@author: JHOSS
"""

#Dada una cadena verificar que sea palindroma(es aquella palabra que se lee lo mismo al derecho y al reves e.j Ana)

#invertir un nombre

def es_palindromo(cadena):
    posicion_izquierda = 0
    posicion_derecha = len(cadena) - 1
    
    while posicion_derecha >= posicion_izquierda:
        if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
            return False
        
        posicion_izquierda += 1
        posicion_derecha += 1
        
    return True

print(es_palindromo('ana'))




