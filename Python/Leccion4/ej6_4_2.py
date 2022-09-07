"""
Ejercicio 2: Operaciones de conjuntos con listas
Escriba un programa que tenga 2 listas y que a continuación
cree las siguientes listas (en la que no deben haber repetición)
1 Lista de palabras que aparecen en las listas
2 lista de palabras que aparecen en la primera lista, pero no en la segunda
3 lista de palabras que aparecen en la segunda lista, pero no en la primera
4 lista de palabras que aparecen en ambas listas
"""

domesticos = ['perro', 'gato', 'hamster']
print('domesticos:', domesticos)
salvajes = ['leon', 'puma', 'águila']
print('salvajes:', salvajes)

print('lista de palabras que aparecen en las listas')
animales = domesticos + salvajes
print(animales)

print('lista de palabras que aparecen en la primera lista, pero no en la segunda')
lista2 = list(set(animales)-set(salvajes))
print(lista2)

print('lista de palabras que aparecen en la segunda, pero no en la primera')
lista3 = list(set(animales)-set(domesticos))
print(lista3)

print('lista de palabras que aparecen en ambas listas')
print(list(set(domesticos) & set(salvajes)))
