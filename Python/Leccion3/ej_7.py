""" Ejercicio 7
Dadas las horas trabajadas de 5 personas y la tarifa de pago,
calcular el salario y la sumatoria de todos los salarios
"""
i = 1
suma_salario = 0
while i <= 5:
    print(f'Trabajador {i}')
    horas = int(input('Ingrese las horas trabajadas: '))
    valor_hora = float(input('Ingrese el valor de la hora: '))
    salario = horas * valor_hora
    print(f'El salario del trabajador {i} es {salario}')
    suma_salario += salario
    i += 1
    print()

print(f'La suma de todos los salarios es {suma_salario}')
