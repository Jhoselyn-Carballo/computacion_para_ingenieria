# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:10:05 2022

@author: JHOSS
"""

from tkinter import *
def contador(accion, contador):
	if accion == 'countUp':
		contador == contador + 1
	elif accion == 'coundDown':
		contador == contador -1
	elif accion == 'reset':
		contador == 0
	return contador
