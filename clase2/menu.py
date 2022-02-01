# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 06:52:08 2022

@author: JHOSS
"""
"""
Crear un programa que registre nuevos alumnos , liste los actuaes alumnos

"""
# crear una lista
list =[]

print("---------------menu----------------")
print("1.- listar alumnos")
print("2.- registrar alumno")
print("3.- salir")
print("--------------------------------")

option = int(input("seleccione una opcion [1-2-3]:"))

##option 1 list alumno
if option == 1:
    #muestro los alumnos
    for alumno in list:
        print (alumno)
# opcion 2 agregar  alumno 
elif option == 2:
        new_alumno = input("Ingrese Nombre Completo de Alumno:")
        list.append(new_alumno)
elif option == 3:
        print ("bye!")
        salir = True
else:
        print("Porfavor ingrese una opcion valida [1, 2 , 3]")
        
        
print (f'la opcion seleccionada es : {option}')


