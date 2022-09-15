""" Ejercicio 12: Sumar números pares dentro de un rango
Hacer un programa para sumar números pares dentro de un rango,
por ejemplo:
    suma de números pares del 2 al 30
    suma = 240

"""
print('Este es un programa que suma los números pares, ')
print('de un rango que definirá usted.')
print('----------------------------------------------- \n')

n1 = int(input('Ingrese el número inicial del rango: '))
n2 = int(input('Ingrese el número final del rango: '))
suma_pares = 0
for x in range(n1, n2+1):
    if x % 2 == 0:
        suma_pares += x

print('\nEl resultado de la suma de los números ')
print(f'pares dentro del rango es {suma_pares}')
