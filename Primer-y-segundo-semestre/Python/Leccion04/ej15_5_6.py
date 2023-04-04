""" Ejercicio 7: Juego adivina el número
Realizar un juego para adivinar un número. Para ello se debe
generar un número aleatorio entre 1 - 100, y luego ir pidiendo
números indicando 'es mayor' o 'es menor' según sea mayor o
menor con respecto a N. El proceso termina cuando el usuario
acierta y alli se debe mostrar el número de intentos.
"""
import random
n_alea = random.randint(1, 101)


intentos = 0
while True:
    n = int(input('Ingrese un número: '))
    intentos += 1
    if n == n_alea:
        print(f'Correcto el número era {n}.\nLo lograste en {intentos} intentos.')
        break
    elif n > n_alea:
        print(f'Incorrecto, te pasaste.\nLlevas {intentos} intentos.')
    elif n < n_alea:
        print(f'Incorrecto, te quedaste corto.\nLlevas {intentos} intentos.')


