# Ejercicio 3
# Leer 10 números e imprimir cuantos son positivos, cuantos
# negativos y cuantos neutros.
positivos = 0
negativos = 0
neutros = 0
for i in range(10):
    num = int(input('Ingrese un número: '))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    elif num == 0:
        neutros += 1

print(f'La cantidad de números positivos es {positivos}')
print(f'La cantidad de números negativos es {negativos}')
print(f'La cantidad de números neutros es {neutros}')
