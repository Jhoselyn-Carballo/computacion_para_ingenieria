# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:14:03 2022

@author: JHOSS
"""

# contar el numero de espacios de "hola mundo soy jhonny"

o = "hola mundo soy jhonny"
espacio = " "

if espacio in o:
    print("la oracion tiene {} espacios en blanco".format(o.count(espacio)))
