# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:22:14 2024

@author: jumaf
"""

VALOR_DOLAR = 847.5
VALOR_REAL = 101.76
VALOR_EURO = 902.85


pesos = float(input('Ingrese la cantidad de pesos $: '))

print(f'Usted tiene ${pesos} pesos argentinos, los cuales se convierten en:')

dolares = round(pesos/VALOR_DOLAR, 12)

print(f'U${dolares} dólares.')
print(f'R${pesos/VALOR_REAL} reales.')
print(f'€${pesos/VALOR_EURO} euros.')

