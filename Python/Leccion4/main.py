# Lista = Ariel , Liliana , Natalia Osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
# print(nombres[0])  # Primer elemento
# print(nombres[1])  # Segundo elemento
# print(nombres[3])  # Cuarto elemento
# print(nombres[-1])  # ultimo elemento
# print(nombres[-2])  # Ante ultimo elemento
print(nombres[0:2])  # Rango de lista, el valor de cierre queda afuera

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
# Desde el indice indicado hasta el final
print(nombres[1:])
# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar nuestra lista
for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres))  # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]  # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
# del nombres
# print(nombres)  # generará un error porque no existe en la memoria la lista

""" Ejercicio 1
Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
ejemplo de ejecución: 0,3,6,9
"""
for i in range(0, 11):
    if i % 3 == 0:
        print(i)

""" Ejercicio 2
Crear un rango de números de 2 a 6 e imprimirlos
Ejemplo de ejecucion: 2,3,4,5,6
"""
for i in range(2, 7):
    print(i)


""" Ejercicio 3
Crear un rango de 3 a 10 pero con un incremento de 2 en 2, en lugar de 1 en 1
Ejemplo de ejecución: 3,5,7,9
"""
for i in range(3, 11, 2):
    print(i)

# Tuplas
""" 
Los elementos de las tuplas son inmutables, no se pueden modificar 
"""
# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)

# Para ver el número de elementos de una tupla
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes, no paréntesis
print(cocina[0])

# mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])
# ejemplo
verduras = ('papa')  # esto no es una tupla es un tipo string
verduras2 = ('papa',)  # esto si es una tupla. Ya que una tupla necesita aunque solo contenga un elemento, una coma
print(verduras)
print(verduras2)

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ')  # Dejamos de ejecutar el salto de linea al final de utilizar print, para usar un espacio

# cocina[0] = 'plato' # esto no esta permitido con las tuplas

# para poder modificarla es necesario convertirla
# esto no es una buena practica
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

del cocina
# print(cocina) # nos generará un error porque la tupla cocina no existe más

""" 
Dada la siguiente tupla 
tupla = (13, 1, 8, 3, 2, 5, 8) # definir la tupla
Crear una lista que solo incluya los números menores a 5 e imprima por consola [1, 3, 2]
"""
tupla = (13, 1, 8, 3, 2, 5, 8)  # definimos la tupla
lista = []
for num in tupla:
    if num < 5:
        lista.append(num)
print(lista)
