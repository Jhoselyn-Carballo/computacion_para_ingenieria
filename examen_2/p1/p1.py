# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:19:40 2022

@author: JHOSS
"""

from tkinter import *
def invertirCadena(palabra):
    res = ''
    index = len(palabra)
    while index >0:
        ultimo_caracter = palabra[index-1]
        res = res + ultimo_caracter
        index=index-1
    return res

palabra = input("ingrese una palabra:")

if palabra == invertirCadena(palabra):
    print(f" la cadena {palabra} es Palindroma")
else:
    print(f" la cadena {palabra} No es Palindroma")
    
 # crear la ventana
window = Tk()
window.geometry('400x400')

label_text=Label(window, text="Enter a word:")
input_text=Entry(window)
label_result=Label(window, text="<<result>>")
button_res=Button(window, text="Validate", command=lambda: invertirCadena())

# coordenada de los components

label_text.place(x=10, y=10)
input_text.place(x=100, y=10)
label_result.place(x=100, y=50)
button_res.place(x=100, y=70)

window.mainloop() 
