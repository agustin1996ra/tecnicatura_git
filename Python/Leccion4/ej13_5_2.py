""" Ejercicio 13: Factorial de un número positivo
Hacer un programa para calcular el factorial de
un número positivo

"""

f_de = int(input('Digite un número: '))
while f_de < 0:
    print("Error: El número debe ser positivo\n")
    f_de = int(input('Digite un número: '))

f = 1  # Factorial
for i in range(1, f_de+1):
    f *= i

print(f'\nEl factorial de {f_de} es: {f}')
