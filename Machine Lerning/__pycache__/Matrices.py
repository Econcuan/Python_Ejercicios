# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:34:29 2022

@author: Estua
"""
'''Se crea una matriz de 3x4 con valores en uno'''
import numpy as np
unos =np.ones((3,4))
print(unos)

     
'''Se crea matriz con ceros'''
import numpy as np
ceros=np.zeros((3,4))
print(ceros)

     
'''Creando matriz con numero de filas y columnas especificas'''

import numpy as np
full=np.full((2,2,),8)
print(full)
    
'''Matriz con valores espaciados uniformemente'''      
import numpy as np
espacio1 = np.arange(0,30,5)
print(espacio1)
espacio2 = np.linspace(0,2,5)
print(espacio2)

'''Matriz identidad '''
import numpy as np
identidad1= np.eye(4,4,)
print(identidad1)

identidad2=np.identity(4)
print(identidad2)

'''Conocer las dimensiones de la Matriz'''
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

'''Conocer el tipo de la Matriz'''
import numpy as np
a=np.array([(1,2,3)])
print(a.dtype)

'''Conocer tamaño y forma de la Matriz'''
import numpy as np
a = np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

'''Cambiando de forma a una Matriz'''

import numpy as np
a = np.array([(8,9,10),(11,12,13)])
print(a)
a=a.reshape(3,2)
print(a)







