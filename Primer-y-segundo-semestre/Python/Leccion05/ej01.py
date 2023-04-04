""" Ejercicio 01: Crear una función para sumar los valores
recibidos de tipo numéricos, utilizando argumentos variables
*args como parámetro de la función y agregar como resultado
la suma de todos los valores pasados como argumentos.
"""


def sumar(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado


print(f'El resultado es: {sumar(1, 2, 3, 4, 5, 6, 7, 8, 9)}')


