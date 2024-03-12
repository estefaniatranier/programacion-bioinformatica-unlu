# -*- coding: utf-8 -*-
"""
Calcular la suma y el producto de los números pares comprendidos entre 20 y 500.
"""

suma = 0
producto = 1

for numero in range(20, 501, 2):
    suma += numero
    producto *= numero
    
print(f'La suma de los valores entre 20 y 500 es {suma}.')
print(f'El producto de los valores entre 20 y 500 es {producto}.')
