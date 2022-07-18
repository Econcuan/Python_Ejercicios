# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:49:13 2022

@author: Estua
"""

'''Creando DataFrame Pandas'''
import numpy as np
import pandas as pd
data = np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))
print(                   
      )

'''Dataframe matriz'''
import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('DataFrame:')
print(df)
print(                   
      )

'''Estadistas del DataFrame'''
import numpy as np
import pandas as pd
print('Estadisticas de DataFrame:')
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(df.describe())
print(                   
      )
print('Media de las columnas del DataFrame:')
print(df.mean())
print(                   
      )
print('Correlación del DataFrame:')
print(df.corr())
print(                   
      )
print('Conteo de datos del DataFrame:')
print(df.count())
print(                   
      )
print('Valor mas alto de la columna del DataFrame:')
print(df.max())
print(                   
      )
print('Valor minimo de la columna del DataFrame:')
print(df.min())
print(                   
      )
print('Mediana de la Columna del DataFrame:')
print(df.median())
print(                   
      )
print('Desviación estandar del DataFrame:')
print(df.std())
print(                   
      )
print('Primera columna del DataFrame:')
print(df[0])
print(                   
      )
print('Dos columnas del DataFrame:')
print(df[[0,1]])
print(                   
      )
print('Valor de la primera fila y última columna del DataFrame:')
print(df.iloc[0][2])
print(                   
      )
print('Valores de la primera fila del DataFrame:')
print(df.iloc[0,:])
print(                   
      )













