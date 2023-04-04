"""
Ejercicio 3: Insertar elementos y ordenarlos
Perdir números y meterlos en una lista, cuando el usuario
introduzca un número 0, nuestro programa dejaría de insertar.
Por último, mostrar los números ordenados de menor a mayor.
"""
lista = []
while True:
    numero = int(input('Ingrese un número: '))
    if numero == 0:
        break
    lista.append(numero)

print(sorted(lista))
