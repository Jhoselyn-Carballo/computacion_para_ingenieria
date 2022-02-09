# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:10:51 2022

@author: JHOSS
"""

#Dado el archivo input.txt que contine la informacion de estudiantes y sus notas generar un archivo de salida output.csv que contenga la informacion de alumno separados por , (comas)

vaciar_archivo = open('output.csv', 'w')
vaciar_archivo.close()


entrada = open('Input.txt', 'r')
for line in entrada.readline():
    lista_sin_espacios =line.split()
    texto_con_comas = 'j'.join(lista_sin_espacios)
    salida = open('output.csv', 'a')
    salida.write(texto_con_comas)
    salida.close()
entrada.close()
    