""" Ejercicio 4
Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) # definir la tupla
Crear una lista que solo incluya los números menores a 5 e imprima por consola [1, 3, 2]
"""
tupla = (13, 1, 8, 3, 2, 5, 8)  # definimos la tupla
lista = []
for num in tupla:
    if num < 5:
        lista.append(num)
print(lista)
