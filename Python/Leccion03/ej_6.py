""" Ejercicio 6
Ingresar N enteros, visualizar la suma de los números pares de
la lista, cuántos números pares existen y cuál es el promedio de los
números impares.
"""
print()
n_enteros = int(input('Digite la cantidad de enteros a ingresar: '))
i = 1
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0
while i <= n_enteros:
    num = int(input(f'{i}-{n_enteros}: Ingrese un numero entero: '))
    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1
    i += 1
if conteo_pares == 0:
    print('No se han ingresado números pares.')
else:
    print(f'La suma de números pares es {suma_pares}')
    print(f'El conteo de los números pares es {conteo_pares}')
if conteo_impares == 0:
    print('No se han ingresado números impares')
else:
    promedio_impares = suma_impares/conteo_impares
    print(f'El promedio de impares es {promedio_impares}')
