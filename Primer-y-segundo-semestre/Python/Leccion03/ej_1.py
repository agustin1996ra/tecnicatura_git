# Ejercicio año bisiesto
# Diseñar un programa que ingresando un año, nos devuelva
# por consola si es un año bisiesto o no, repetir la acción
# hasta que el usuario lo decida.

print('Comprobamos que año es bisiesto')
opcion = 1
while opcion == 1:
    anio = int(input('Ingrese el año: '))
    if ((anio % 4 == 0) and (anio % 100 != 0)) or (anio % 400 == 0):
        print(f'{anio} es un año bisiesto')
    else:
        print(f'{anio} no es un año bisiesto')
    opcion = int(input('Si desea seguir ingresando años presione 1: '))
