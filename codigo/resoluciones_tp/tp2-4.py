# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:30:16 2024

@author: jumaf
"""

# Ingresar dos números por teclado, que podrán ser iguales, e informar cual es el mayor.

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))

if (numero1 > numero2):
    print('El primer número es el mayor.')
elif (numero1 == numero2):
    print('Ambos números son iguales.')
else:
    print('El segundo es el mayor.')
    
print('Finalizó el programa.')