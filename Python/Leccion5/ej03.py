""" Ejercicio 3: Función recursiva
Imprimir números de 5 a 1 de manera descendente usando
funciones recursivas.
Puede ser cualquier valor positivo, por ejemplo, si pasamos el
valor de 5, debe imprimir:
5
4
3
2
1
"""


def imprimir_numeros(n):
    if n == 1:
        print(n)
    else:
        print(n)
        imprimir_numeros(n - 1)


numero = int(input('Ingrese un numero: '))
imprimir_numeros(numero)
