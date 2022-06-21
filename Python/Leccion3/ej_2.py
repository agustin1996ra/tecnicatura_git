# Ejercicio 2
# Calcular la suma de "N" primeros números

n = int(input('Ingrese la cantidad de números a sumarse: '))
suma = 0
i = 0
while i <= n:
    suma = suma + i
    i += 1

print(f'La suma de los primeros {n} números es {suma}')

