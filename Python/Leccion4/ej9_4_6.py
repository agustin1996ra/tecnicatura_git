"""
Ejercicio 1: Lenar una lista
Llenar una lista con los números del 1 al 50, luego mostrá
la lista con el bucle for, los elementos deben mostrarse de
la siguiente forma:
1-2-3-4-5...-50
"""

lista = list(range(1, 51))

for numero in lista:
    if numero == 50:
        print(numero)
        break
    print(f'{numero}-', end='')
