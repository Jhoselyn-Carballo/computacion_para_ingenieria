# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 06:53:01 2022

@author: JHOSS
"""

# Leer un Archivo

# f es un archivo objeto
f=open('listaAlumnos.txt', 'r+')

print("--------",f. leer())
# propiedades del objeto file
print("nombre de archivo", f. nombre)
print("mode de archivo", f. modo)
print("estado de archivo : Closed", f. cerrado)
f. cerrar()
print("estado de archivo : Closed", f. cerrado)

# Crear un archivo
f_2 = open('listaProfes.txt', 'w+')
f_2. write('jhonny\n')
f_2. escribir('René\n')
f_2. cerrar()

# Copiar contenido de un archivo
# Iterar linea por linea un archivo
# copia de archivos
f_num = open('listaNumeros.txt', 'r') # origen
f_num_out = open('salida.txt', 'w+') # destino

para líneas en f_num:
    print(linea))
    f_num_out. write(linea))

f_num. cerrar()
f_num_out. cerrar()