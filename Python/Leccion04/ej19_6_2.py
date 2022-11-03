""" Ejercicio 11: Agenda telefonica
Hacer un programa que simule una agenda de contactos. Crear un
diccionario donde la clave sea el nombre del usuario y el
valor sea el teléfono, el programa tendrá el siguiente menú
de opciones:
    1. Nuevo contacto
    2. Borrar contacto
    3. Ver contactos existentes
    4. Salir
"""
import time

clearConsole = lambda: print('\n' * 20)
agenda = dict()

while True:
    clearConsole()
    print('.: Menu :.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')

    selector = int(input('\nIngrese la opción que desea: '))
    match selector:
        case 1:
            clearConsole()
            nombre = input('Ingrese el nombre del contacto: ')
            telefono = int(input('Ingrese el teléfono: '))
            agenda[nombre] = telefono
        case 2:
            clearConsole()
            print('Borrar un contacto')
            nombre = input('Ingrese el nombre del contacto: ')
            if nombre in agenda:
                del agenda[nombre]
                print('Ha sido eliminado correctamente')
        case 3:
            clearConsole()
            for key, value in agenda.items():
                print(f'{key}: {value}')
            time.sleep(3)
        case 4:
            clearConsole()
            print('Hasta luego')
            break
