# En esta clase veremos la sentencia if else
# condicion = True
# if condicion is True:
#     print('Condición verdadera')
# elif condicion is False:
#     print('Condición Falsa')
# else:
#     print("Condición sin especificar")

# Ejecución paso a paso en el condicional
# condicion = True  # punto de ruptura
# if condicion is True:
#     print('Condición verdadera')
# elif condicion is False:
#     print('Condición Falsa')
# else:
#     print("Condición sin especificar")

#

# num = int(input("Digite un número en el rango del uno al tres: "))
# numTexto = ""
# if num == 1:
#     numTexto = "Número uno"
# elif num == 2:
#     numTexto = "Número dos"
# elif num == 3:
#     numTexto = "Número tres"
# else:
#     numTexto = "Has ingresado un numero fuera de rango"
# print(f'El número ingresado es: {num} - {numTexto}')

# Sintaxis operador ternario
# condicion = True
# print('Condición Verdadera') if condicion else print('Condición Falsa')

# Ejercicio área y longitud de un círculo
# Hacer un programa para ingresar el radio de un círculo
# y se reporte su área y el perímetro de la circunferencia.

import math

r = float(input('Ingrese el radio de una circunferencia: r = '))
area = math.pi * (r ** 2)
perimetro = 2 * math.pi * r
print(f'Un circulo de radio = {r} , tiene un area = {area} y un perimetro = {perimetro} ')
