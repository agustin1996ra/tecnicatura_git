""" Ejercicio 8: Menú interactivo - Cajero automatico
Hacer un programa que simule un cajero automatico
con un saldo inicial de $1000 y tendrá el siguiente
menú de opciones:
    1. Ingresar dinero en la cuenta
    2. Retirar dinero de la cuenta
    3. Mostrar dinero disponible
    4. Salir
"""
import time

clearConsole = lambda: print('\n' * 20)

clearConsole()
cuenta = 1000

while True:
    clearConsole()
    print('1. Ingresar dinero en la cuenta\n2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible\n4. Salir')

    n = int(input('Ingrese un número: '))
    match n:
        case 1:
            clearConsole()
            cuenta += int(input('Cuanto dinero desea ingresar: '))
        case 2:
            while True:
                clearConsole()
                retira = int(input('Cuanto desea retirar: '))
                if retira <= cuenta:
                    cuenta -= retira
                    print(f'Saldo disponible: ${cuenta}')
                    break
                else:
                    print('Fondos insuficientes!')
                    time.sleep(3)
        case 3:
            clearConsole()
            print(f'En la cuenta posee: ${cuenta}')
            time.sleep(3)
        case 4:
            clearConsole()
            print('Hasta luego!')
            break
