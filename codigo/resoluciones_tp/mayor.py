# -*- coding: utf-8 -*-

# Ingresar dos números por teclado, que podrán ser iguales, e informar cual es el mayor.

from funciones_propias import mayor_entre_2

n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número: '))

perro, gato = mayor_entre_2(numero1=n1, numero2=n2)
    
print(perro)

print(f'El mayor es {gato}')

