""" Ejercicio 2: función con *args para multiplicar
Crear una función para multiplicar los valores recibidos
de tipo numérico, utilizando argumentos variables *args
como parámetro de la función y regresar como resultado
la multiplicación de todos los valores pasados como argumentos.
"""


def multiplicar1(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado


listaNumeros = []
ns = int(input('Cuantos números desea multiplicar: '))
for i in range(1, ns + 1):
    listaNumeros.append(int(input('Ingrese un numero: ')))

res = multiplicar1(2, 3, 4)
print(f'El resultado de la multiplicación de los números ingresados es: {res}')

