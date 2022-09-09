"""
Ejercicio 2: Modificar los elementos de una lista
Llenar una lista con los números del 1 al 10, luego modificar los
elementos de la lista multiplicándolos por un valor ingresado por
el usuario.
"""

lista = list(range(1, 11))

multiplicando = int(input('Ingrese un multiplicando: '))

for numero in lista:
    lista[numero - 1] = multiplicando * numero

print(lista)

