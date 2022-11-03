""" Ejercicio 6: tabla de multiplicar
Hacer un programa que pida un número por teclado
y guarde en una lista su tabla de multiplicar
hasta el 10. Por ejemplo: si digita el 5 la
lista tendrá: 5, 10, 15, 20, 25, 30, 35, 40,
45, 50

"""

n = int(input('Ingrese un numero: '))

lista = []

for i in range(1, 11):
    lista.append(i * n)

print(lista)
