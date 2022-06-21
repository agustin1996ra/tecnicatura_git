""" Ejercicio 4
Suponga que se tiene un conjunto de calificaciones de un grupo de
10 alumnos. Realizar un algoritmo para calcular la calificación
promedio y la calificación más baja de todo el grupo.
"""
total = 0
nota_baja = 100
for i in range(10):
    nota = int(input(f'Introduzca la nota del alumno {i+1}: '))
    total = total + nota
    if nota <= nota_baja:
        nota_baja = nota

promedio = total / 10
print(f'El promedio de las notas de los 10 alumnos es {promedio}')
print(f'La nota mas baja es {nota_baja}')
