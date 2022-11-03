"""
Ejercicio 1: Eliminar duplicados de una lista
escriba un programa donde tenga una lista y que a continuación
elimine los elementos repetidos, por último mostrar la lista.
"""

lista = ['agustin', '26 años', 'rodriguez', 'agustin', '26 años', 'rodriguez', 'agustin', '26 años', 'rodriguez']
print(lista)
lista = list(set(lista))
print(lista)
