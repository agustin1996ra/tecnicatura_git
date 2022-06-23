""" Ejercicio 5
Calcular el factorial de un número mayor o igual a 0
"""
num = -1
while num < 0:
    num = int(input('Digite un numero: '))

i = 1
factorial = 1

while i <= num:
    factorial *= i
    i += 1

print(f'El factorial de {num} es {factorial}')
