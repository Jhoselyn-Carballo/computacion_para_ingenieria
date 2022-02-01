# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 06:08:24 2022

@author: JHOSS
"""

NAME = 'jhoselyn'
FULL_NAME = 'jhoselyn carballo sanchez'
print (NAME)
print (FULL_NAME)

# TIPOS DE DATOS
entero = 90
print (f' el entero tiene valor de {entero}')
decimal = 6.14
print (f' el valor del decimal es {decimal}')
caracter = 'J'
print (f' el valor del decimal es {caracter}')
cadena = 'primera cadena'
print (f' el valor del decimal es {cadena}')
cadena_2 = "segunda cadena"
print (f' el valor del decimal es {cadena_2}')

booleano = False # valores True o False
print (f' el valor del decimal es {booleano}')
# LISTA
list=[1, 2, 3, 4]
print (f' el valor de la lista es : {list}')

# DICCIONARIO
diccionario = {'nombre': 'Jhoselyn Carballo Sanchez', "edad": 20}
nombre = diccionario["nombre"]
edad = diccionario ["edad"]
print (f' el nombre es: {nombre} y su edad {edad}')

# ENTRADAS ESTANDAR
telefono = input("Ingrese numero telefonico")
#  CAST DE TIPOS
a = int(input("Ingrese a :"))
b = int(input("Ingrese b :"))

print(f' resultado de sumar a + b = {a+b}')

# ESTRUCTURAS DE CONTROL
anio = 2023

if anio <=2022:
    print("anio es menor a 2022")
elif anio >= 1989:
    print ("el anio es mayor a 1989")
else:
    print("el anio no cumple con los rangos de 1989 o 2022")

# ESTRUCTURAS DE CONTROL WHILE     