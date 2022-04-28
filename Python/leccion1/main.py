"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos"
print(miVariable)
miVariable = 3.5
print(miVariable)


print()
print()
"""
"""
Tipos de variables:
    int = número entero
    float = número decimal
    String = Cadena de caracteres
    Bool = variable Booleana
    
Cuando utilizamos la función "type()" obtenemos 
la información de que tipo de variable ingresamos
dentro de los paréntesis de la función
"""
"""
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))


print()
print()
"""

"""
Manejo de cadenas (String)
    - Concatenación:
-   Utilizando el operador +, en el caso de no estar usando literales
    (valores numéricos) el operador + significa concatenación y no como
    suma.
    
-   Utilizando la coma
"""
"""
miGrupoFavorito = "Snarky Puppy"
caracteristicas = "The best contemporary Jazz Band"
print("Mi grupo favorito es: "+miGrupoFavorito+". "+caracteristicas)
# Acá un ejemplo de como se puede usar el +
miGrupoFavorito2 = "Snarky Puppy"+". "+"The best contemporary Jazz Band"
print("Mi grupo favorito es: "+miGrupoFavorito2)

# Otra forma de concatenar cadenas utilizando la coma.
# Nótese que la concatenación con comas agrega un espacio.
# Lo que puede generar problemas como con el "."
print("Mi grupo favorito es:", miGrupoFavorito+".", caracteristicas)

numero1 = "7"
numero2 = "8"
# Si trabajamos con cadenas solo concatena, no suma
print(numero1+numero2)
# pero si trabajamos con literales si lo hara
print(int(numero1) + int(numero2))

print()
print()
"""
""" 
#Tipos Booleanos    

miBooleano1 = True
print(miBooleano1)
miBooleano2 = 3 > 2
print(miBooleano2)

if miBooleano2:
    print("3 > 2  es verdadero")
else:
    print("3 > 2  es falso")

miBooleano3 = 1 > 2
if miBooleano3:
    print("1 > 2 es verdadero")
else:
    print("1 > 2 es falso")
"""

# Procesar la entrada del usuario
# función input
"""
resultado = input("Digite un numero: ") # Nos regresa un dato tipo str
print("el numero ingresado es: "+resultado)
"""
# Conversión de la entrada de datos
"""
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
"""
# Operadores
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma: ", suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

division = operandoA / operandoB

division = operandoA // operandoB

modulo = operandoA % opernadoB

exponente = operandoA ** operandoB

"""
"""

# Ejercicio rectángulo
alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))
area = alto * ancho
perimetro = (alto + ancho)*2
print(f"El perimetro de el rectángulo es {perimetro} y el area es {area}")


# operadores de comparacion
"""

# ejercicio par o impar

num = int(input("ingrese un numero: "))
if (num % 2) == 0:
    print("el numero es par")
else:
    print("el numero es impar")

comprobador = (num % 2) == 0

if comprobador:
    print("el numero es par")
else:
    print("el numero es impar")

