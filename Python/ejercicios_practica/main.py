# Ejercicios de práctica complementarios
# De la página patriciaemiguel.com

# Sección 1
# Entrada/salida de datos - Variables - Tipos de datos


""" Ejercicio 1
Escribí un programa que solicite al usuario que ingrese su nombre.
El nombre se debe almacenar en un variable llamada 'nombre'. A
continuación se debe mostrar en pantalla el texto 'Ahora estas en la
matrix, [nombre]'.
"""

# nombre = input('Ingresá tu nombre: ')
# print(f'Ahora estas en la matrix, {nombre}')

""" Ejercicio 2
Escribí un programa que solicite al usuario ingresar un número con 
decimales y almacenalo en una variable. A continuación, el program 
debe solicitar al usuario que ingrese un número entero y guardarlo
en otra variable. En una tercera variable se deberá guardar el resultado
de la suma de los dos números ingresados por el usuario. Por último, 
se debe mostrar en la pantalla el texto 'El resultado de la suma es {suma}'.
"""

# n1 = float(input('Ingrese un numero real: '))
# n2 = int(input('Ingrese un numero entero: '))
# suma1 = n1 + n2
# print(f'El resultado de la suma es {suma1}')

""" Ejercicio 3
Escribí un programa que solicite al usuario dos números y los almacene
en dos variables. En otra variable, almacená el resultado de la suma de 
estos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un 
tercer número, el cual se debe almacenar en una nueva variable. Por
último, mostrá en pantalla el resultado de la multiplicación de este
nuevo número por el resultado de la suma anterior.
"""

n1 = int(input('Ingrese un numero entero: '))
n2 = int(input('Ingrese otro numero entero: '))
suma = n1 + n2
print(f'El resultado de la suma de los numeros es {suma}')
n3 = int(input('Ingrese otro numero entero: '))
mul = suma * n3
print(f'El resultado de la multiplicacion de la suma con el tercer numero es {mul}')

""" Ejercicio 4
Escribí un programa que solicite al usuario ingresar la cantidad de 
kilómetros recorridos por una motocicleta y la cantidad de litros
de combustible que consumió durante ese recorrido. Mostrar el consumo
de combustible por kilómetro.
"""

km = int(input('Ingrese la cantidad de kilometros recorridos: '))
lts = float(input('Ingrese la cantidad de litros consumidos: '))
lts_km = lts / (km / 100)
print(f'El consumo por 100 kilómetros es de {lts_km} lts.')

""" Ejercicio 5
Escribí un programa que solicite al usuario el ingreso de una 
temperatura en escala Fahrenheit y le muestre el equivalente en 
grados Celsius. La fórmula de conversión que se usa para este 
cálculo es: Celsius = (5/9)*(Fahrenheit -32)
"""

