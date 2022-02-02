# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 06:24:33 2022

@author: JHOSS
"""
    # i, j -> recordar que lo hara de 2 en 2, por eso definimos i, j
A = [55, 86, 32, 12, 82, 43]
"""i,j"""
#obtener el tamanio de la lista
num = len(A)
i=0
while i < num:
    j=i
    while j<num:
        if(A[i]> A[j]):
            #swap intercambio de posiciones
            aux=A[i]
            A[i]=A[j]
            A[j]=aux
        j=j+1
    i=i+1
print ("Lista Ordenada")
print (A)

listDeNumeros = [34, 12, 4, 10]
print ("Lista Original")
print(listDeNumeros)
listDeNumeros.sort()
print("lista Ordenada")
print(listDeNumeros)