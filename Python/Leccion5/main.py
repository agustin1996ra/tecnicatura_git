""" Funciones
Comenzamos con funciones
mi_funcion() no se puede llamar antes de definir una función
"""


# Definimos una función
def mi_funcion():
    print('Saludos desde la función\n')


mi_funcion()  # Estamos llamando a la función
mi_funcion()  # Se puede llamar a la función N cantidad de veces


# Desempaquetado de listas o list unpacking
def show(name, lastname):
    print(name + ' ' + lastname)


# Con listas
person = ["Agustin", "Rodriguez"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la funcion
show(*person)  # Esto es lo mismo qie lo anterior pero le pasamos todo junto
# Con tuplas
person2 = ('Ariel', 'Betancud')  # Desempaquetamos a través de una tupla
show(*person2)
# Con diccionarios
persona3 = {'lastname': 'Lucero', 'name': 'Natalia'}
show(**persona3)  # Al tener como llaves los nombres de los parámetros de la función


numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break  # Esta es la única manera que el else no se ejecute
else:
    print('Esto se termino')

# Comprensión de listas
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P']  # Esto regresará una nueva lista
print(alongP)

bottleC = [{'name': 'Quilmes', 'country': 'Arg'},
           {'name': 'Corona', 'country': 'Mex'},
           {'name': 'Stella Artois', 'country': 'Belgium'}]

arg = [b for b in bottleC if b['country'] == 'Arg']
print(arg)
print(bottleC)


# Paso de argumentos (funciones)
def mi_funcion2(name, lastname):
    print('Saludos')
    print(f'Nombre: {name}, Apellido: {lastname}')


mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b


resultado = sumar(72, 22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')


def sumar2(a=0, b=0):  # Le damos un valor por default
    return a + b


resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'resultado de la suma: {sumar2(22, 66)}')  # se pueden alterar los valores por default


# Argumentos, variables en funciones
def listar_nombres(*nombres):  # Normalmente se utiliza: *args
    for nombre in nombres:  # Se va a convertir en una tupla
        print(nombre)


listar_nombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')

