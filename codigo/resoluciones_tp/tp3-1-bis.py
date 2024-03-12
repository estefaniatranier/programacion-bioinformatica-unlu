# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:38:44 2024

@author: jumaf
"""

suma = 0
producto = 1

for numero in range(20, 501):
    
    if numero%2 == 0:
        suma += numero
        producto *= numero
    
print('La suma de los valores entre 20 y 500 es ', suma)
print(f'El producto de los valores entre 20 y 500 es {producto}.')
