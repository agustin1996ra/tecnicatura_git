""" Ejercicio 5: Convertidor de temperaturas
Realizar dos funciones para convertir de grados celsius
a fahrenheit y viceversa.
Investigar las fórmulas.
"""
import time


def c_a_f(temp_c):
    print(f'{temp_c * 1.8 + 32}°F')


def f_a_c(temp_f):
    print(f'{(temp_f - 32) / 1.8}°C')


def borrar():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')


def menu():
    print('.: Menú :.\n1. Pasar de Celsius a Fahrenheit')
    print('2. Pasar de Fahrenheit a Celsius\n3. Salir')


while True:
    borrar()
    menu()
    selector = int(input('Elija un opción: '))
    match selector:
        case 1:
            temp = float(input('Introduzca la temperatura en C°: '))
            c_a_f(temp)
            time.sleep(3)
        case 2:
            temp = float(input('Introduzca la temperatura en °F: '))
            f_a_c(temp)
            time.sleep(3)
        case 3:
            break

