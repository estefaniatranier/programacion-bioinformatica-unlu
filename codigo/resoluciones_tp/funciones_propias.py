# -*- coding: utf-8 -*-

def mayor_entre_2(numero1, numero2):
    """
    Esta función retorna el valor mayor entre dos números y un cartel indicativo    

    Parameters
    ----------
    numero1 : int
        Primer valor a evaluar
    numero2 : int
        Segundo valor a evaluar

    Returns
    -------
    cartel : str
        Cartel indicativo del resultado
    mayor : int
        Mayor de los dos números
    """
    
    if (numero1 > numero2):       
        cartel = 'El primer número es el mayor.'
        mayor = numero1
    elif (numero1 == numero2):
        cartel = 'Ambos números son iguales.'
        mayor = numero1
    else:
        cartel = 'El segundo número es el mayor.'
        mayor = numero2
        
    print('Finalizó el programa.')
    
    return cartel, mayor