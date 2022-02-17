# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:10:36 2022

@author: JHOSS
"""

from tkinter import *

def sumar():
    op1=int(input_op1.get())
    op2=int(input_op2.get())
    suma= op1 + op2
    print("la suma es ", suma)
    label_res.config(text=f"The sum is: {op1} + {op2} = {suma}")
    
#resta
def restar():
    op1=int(input_op1.get())
    op2=int(input_op2.get())
    resta= op1 - op2
    print("la resta es ", resta)
    label_res1.config(text=f"The resta is: {op1} - {op2} = {resta}")
    
#multiplicacion
def multi():
    op1=int(input_op1.get())
    op2=int(input_op2.get())
    multip= op1 * op2
    print("la multip es ", multip)
    label_res.config(text=f"The multip is: {op1} * {op2} = {multip}")

    
#crear un windows
window = Tk()
window.geometry('500x400')

# creamos los componentes
label_op1= Label(window, text="Enter the value of M:")
label_op2= Label(window, text="Enter the value of N:")
label_res=Label(window, text="<<result>>")
input_op1= Entry(window)
input_op2= Entry(window)
buton_res= Button(window, text="sumar", command=lambda: sumar())
#resta
buton_res1= Button(window, text="restar", command=lambda: restar())
#multiplicacion
buton_res2= Button(window, text="multi", command=lambda: multi())

# coordenadas de los elementos
label_op1.place(x=10, y=10)
input_op1.place(x=200, y=10)

label_op2.place(x=10, y=50)
input_op2.place(x=200, y=50)

label_res.place(x=210, y = 90 )
buton_res.place(x=210, y = 110)

label_res.place(x=260, y = 90 )
buton_res1.place(x=260, y = 110)

label_res.place(x=310, y = 90 )
buton_res2.place(x=310, y = 110)

window.mainloop()