# Ejercicio 4: área y longitud de un círculo
# Hacer un programa para ingresar el radio de un círculo
# y se reporte su área y el perímetro de la circunferencia.

import math

r = float(input('Ingrese el radio de una circunferencia: r = '))
area = math.pi * (r ** 2)
perimetro = 2 * math.pi * r
print(f'Un circulo de radio = {r} , tiene un area = {area} y un perimetro = {perimetro} ')
