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

# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
print(len(planetas))

# Revisar si un elemento existe dentro de set
print('Marte' in planetas)  # Recordar que python distingue entre mayúsculas y minúsculas y tildes

# Agregar un elemento
planetas.add('Tierra')  # add es una funcions
print(planetas)
planetas.add('Tierra')  # Esto no tendrá ningún tipo de efecto, ya que le elemento
# 'Tierra' ya se encuentra dentro del set


# Eliminar elemnetos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')
print(planetas)

# en cambio con discard no se generara un error
planetas.discard('Tierra')
print(planetas)
planetas.discard('tierra')

# Limpiar nuestro tipo set
planetas.clear()
print(planetas)

# Para eliminar
# del planetas
print(planetas)  # esto debería dar un error porque ya no existe

# Diccionarios
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
print(diccionario)

# Determinar la cantidad de elementos
print(len(diccionario))

# Acceder a un elemento con la llave(key)
print(diccionario['IDE'])  # nos mostrará el valor referenciado a esa llave

# otra forma de recuperar un elemento
print(diccionario.get('POO'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario['IDE'])

# Como recorrer los elementos
for termino in diccionario:
    print(termino)  # Esto nos permitirá acceder solo a las llaves

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)


# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():  # Usamos esta función para acceder a las llaves
    print(termino)  # Muestra solo las llaves

for valor in diccionario.values():  # usamos esta función para acceder a los valores
    print(valor)

# Comprobar la existencia de algun elemeno
print('IDE' in diccionario)  # Devuelve un valor booleano de la comprobacion.

# Agregar un elemento
diccionario['PK'] = 'Llave primaria'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario

# Concatenar listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

# Agregar varios elementos a una lista
lista3.extend([7, 8, 9, 1])  # Función para agregar varios elementos a una lista
print(lista3)

# Averiguar el índice de un elemento de la lista
print(lista3.index(5))  # Función para ubicar en que indice está el valor ingresado
# print(lista3.index(0))  Esto dará un error por el elemento no ser parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))  # Cuanta cuantos valores iguales hay dentro de la lista

# Para poner nustra lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort()  # Ordena los elementos de forma ascendente
print(lista3)

lista3.sort(reverse=True)  # Ordena los elementos de forma descendente
print(lista3)

# Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')  # Puede tener diferentes tipos de elementos
print(tupla)

# Averiguar si un elemento se encuentra dento de una tupla
print(4 in tupla)

# Averiguar si un elemento se encuentra dentro de una tupla
print(4 not in tupla)
# Lo que podemos usar dentro de tuplas son: index, count, len
# Las tuplas se pueden convertir en listas y las listas en tuplas

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones',
         'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    2: {'Nombre': 'Juan Foyth', 'Edad': 24, 'Altura': 1.87, 'Precio': '25 Millones', 'Posicion': 'Lateral Derecho'},
    3: {'Nombre': 'Nicolas Tagliafico', 'Edad': 30, 'Altura': 1.72, 'Precio': '11 Millones',
        'Posicion': 'Lateral Izquierdo'},
    4: {'Nombre': 'Gonzalo Montiel', 'Edad': 25, 'Altura': 1.76, 'Precio': '14 millones', 'Posicion': 'Lateral Derecho'},
    5: {'Nombre': 'Alexis Mac Alister', 'Edad': 23, 'Altura': 1.74, 'Precio': '16 Millones',
        'Posicion': 'Mediocentro Ofensivo'}

}
print(seleccionArgentina)
print(seleccionArgentina[4])
