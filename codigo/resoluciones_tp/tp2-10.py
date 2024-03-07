# -*- coding: utf-8 -*-
"""
Diseñe un algoritmo que califique el puntaje obtenido en el lanzamiento de tres dados 
en función a la cantidad seis obtenidos, de acuerdo a lo siguiente:
- Seis en los tres dados, excelente.
- Seis en dos dados, muy bien.
- Seis en un dado, regular.
- Ningún seis, pésimo.
"""

dado1 = int(input('Ingrese el valor del dado 1: '))
dado2 = int(input('Ingrese el valor del dado 2: '))
dado3 = int(input('Ingrese el valor del dado 3: '))

if (dado1 == 6) and (dado2 == 6) and (dado3 == 6):
    print('Seis en los tres dados, excelente.')
elif (dado1 == 6 and dado2 == 6):
    print('Seis en dos dados, muy bien.')
elif (dado2 == 6 and dado3 == 6):
    print('Seis en dos dados, muy bien.')
elif (dado1 == 6 and dado3 == 6):
    print('Seis en dos dados, muy bien.')
elif (dado1 == 6) or (dado2 == 6) or (dado3 == 6):
    print('Seis en un dado, regular.')
else:
    print('Ningún seis, pésimo.')

