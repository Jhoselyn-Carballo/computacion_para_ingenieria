# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:23:55 2022

@author: JHOSS
"""

def mostrarDigitoByDigito(entrada):
    while entrada > 0:
        digito = entrada % 10
        print(digito)
        #entrada = int(entrada/10) #
        entrada//=10


entrada = 199

mostrarDigitoByDigito(entrada)