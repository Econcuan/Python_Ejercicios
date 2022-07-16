# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 22:35:19 2022

@author: Estua
"""

'''Array en 1D y 2D '''
import numpy as np
a=np.array([1,2,3])
print('1D array:')
print(a)
print()
b=np.array([(1,2,3),(4,5,6)])
print('2D array:')
print(b)

''' Modulo SYS da acceso a varibles utilizadas por el interprete '''

import sys 
S=range(1000)
print('Resultado lista de Python:')
print(sys.getsizeof(5)*len(S))
print()
D=np.arange(1000)
print('Resultado NumPy array:')
print(D.size*D.itemsize)

'''Evaluando la rapidez de respuesta usando el Modulo time'''

import time 

SIZE = 1000000
L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)
start= time.time()
result=[(x,y) for x,y in zip (L1,L2)]
print('Resultado lista de python:')
print((time.time()-start)*1000)
print()
start=time.time()
result=A1+A2
print('Resultado NumPy array:')
print((time.time()-start)*1000)




