"""
Ingrese las calificaciones de un parcial para un grupo de N (definido por el usuario) 
alumnos del curso Programación y calcule el promedio de calificaciones y 
porcentaje de aprobados, desaprobados y ausentes 
(los ausentes se representarán con el valor 99 como calificación).
"""

ausentes = 0
aprobados = 0
desaprobados = 0
total_notas = 0

N = int(input("Ingrese la cantidad N del grupo de estudiantes: "))

for i_estudiante in range(1, N+1):
    
    calificacion = float(input(f'Ingrese la calificación del estudiante {i_estudiante}: '))
    
    if calificacion!=99:
        total_notas+=calificacion
    
    if (calificacion == 99):
        ausentes+=1
    elif (calificacion >= 6):
        aprobados+=1
    else:
        desaprobados+=1
    

print(f'% de aprobados: {round((aprobados/(N-ausentes))*100, 2)}')
print(f'% de ausentes: {round((ausentes/N)*100, 2)}')
print(f'% de desaprobados: {round((desaprobados/(N-ausentes))*100, 2)}')
print(f'Promedio de calificaciones: {round(total_notas/(N-ausentes), 2)}')
