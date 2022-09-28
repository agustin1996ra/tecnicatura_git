

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input('Ingrese un número para calcular su factorial: '))
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}.')
