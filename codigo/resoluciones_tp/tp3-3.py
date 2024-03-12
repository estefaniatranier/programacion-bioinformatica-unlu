# -*- coding: utf-8 -*-
"""
Desarrollar un programa que permita ingresar por teclado la cantidad milímetros 
de lluvia caída en Luján para una semana y calcule el promedio. 

El programa además deberá alertar al usuario cuando la cantidad de lluvia caída 
en la semana supere una cantidad ingresada por el usuario, 
a efectos de poner en marcha acciones preventivas contra las posibles inundaciones.

"""
mm_caidos = 0
dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

mm_alerta = float(input('Ingrese los milímetros para la emisión del alerta de lluvias: '))

for dia in dias_semana:
    mm_lluvia = float(input(f'Ingrese los milímetros de lluvia para el día {dia}: '))
    mm_caidos += mm_lluvia
    
    if (mm_caidos >= mm_alerta):
        print(f'Las lluvias al día {dia} alcanzaron el valor definido para el ALERTA.')
    

print(f'El promedio de lluvias de la semana es {round(mm_caidos/len(dias_semana), 2)}')
