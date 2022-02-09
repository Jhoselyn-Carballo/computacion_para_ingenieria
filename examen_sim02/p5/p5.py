# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 03:24:10 2022

@author: JHOSS
"""

def quitarSaltoLinea_lista(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].strip()


lisNotas = open('Notas.txt', 'r')
estudiantes = open('Estudiantes.txt', 'r')

salida = open('primer_parcial.txt', 'w+')

lista_Notas = lisNotas.readlines()
quitarSaltoLinea_lista(lista_Notas)
lista_estudiantes = estudiantes.readlines()
quitarSaltoLinea_lista(lista_estudiantes)


for i in range(len(lista_Notas)):
    salida.write(lista_Notas[i]+" "+lista_estudiantes[i]+"\n")
    
lisNotas.close()
estudiantes.close()
salida.close()