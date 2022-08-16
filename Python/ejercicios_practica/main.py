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

# n1 = int(input('Ingrese un numero entero: '))
# n2 = int(input('Ingrese otro numero entero: '))
# suma = n1 + n2
# print(f'El resultado de la suma de los numeros es {suma}')
# n3 = int(input('Ingrese otro numero entero: '))
# mul = suma * n3
# print(f'El resultado de la multiplicacion de la suma con el tercer numero es {mul}')

""" Ejercicio 4
Escribí un programa que solicite al usuario ingresar la cantidad de 
kilómetros recorridos por una motocicleta y la cantidad de litros
de combustible que consumió durante ese recorrido. Mostrar el consumo
de combustible por kilómetro.
"""

# km = int(input('Ingrese la cantidad de kilometros recorridos: '))
# lts = float(input('Ingrese la cantidad de litros consumidos: '))
# lts_km = lts / (km / 100)
# print(f'El consumo por 100 kilómetros es de {lts_km} lts.')

""" Ejercicio 5
Escribí un programa que solicite al usuario el ingreso de una 
temperatura en escala Fahrenheit y le muestre el equivalente en 
grados Celsius. La fórmula de conversión que se usa para este 
cálculo es: Celsius = (5/9)*(Fahrenheit -32)
"""
# # temperatura en en Fahrenheit
# tf = float(input('Ingrese una temperatura en fahrenheit: '))
# # temperatura en Celsius
# tc = (5/9)*(tf - 32)
# print(f'La temperatura en grados Celsius es {tc}')

""" Ejercicio 6
Escribir un programa que solicite al usuario ingresar tres números para
luego mostrarle el promedio de los tres.
"""

# n1 = float(input('Primer número: '))
# n2 = float(input('Segundo número: '))
# n3 = float(input('Tercer número: '))
# promedio = (n1 + n2 + n3)/ 3
# print(f'El promedio de los tres es {promedio}')

""" Ejercicio 7
Escribí un programa que solicite al usuario un número y le reste el 15%,
almacenando todo en un única variable. A continuación, mostrar el
resultado final en pantalla.
"""

# num = float(input('Ingresá un número: '))
# num *= 0.85
# print(f'Descontando el 15% queda: {num}')

""" Ejercicio 8
Escribí un programa que solicite al usuario el ingreso de dos palabras,
las cuales se guardarán en dos variables distintas. A continuación,
almacená en un variable la concatenación de la primera palabra, más un
espacio, más la segunda palabra. Mostrá este resultado en pantalla.
"""

# palabra = input('Primera palabra: ')
# palabra += " " + input('Segunda palabra: ')
# print(palabra)

""" Ejercicio 9
Escribí un programa que solicite al usuario el ingreso de un texto
y almacene ese texto en un variable. A continuación, mostrar en pantalla
la primera letra del texto ingresado. Luego, solicitar al usuario que
ingrese un número positivo menor a la cantidad de caracteres que tiene
el texto que ingresó (por ejemplo, si escribió la palabra "hola", 
tendrá que ser un número entre 0 y 4) y almacenrar este número en una
variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada 
por el indice.
"""

# palabra = input('Ingresá un texto: ')
# print(f'El carácter en primer lugar es: {palabra[0]}')
# indice = int(input(f'Ingrese un número positivo menor a {len(palabra)}: '))
# print(f'El carácter en esa posición es: {palabra[indice]}')

""" Ejercicio 10
Escribí un programa que solicite al usuario que ingrese cuántos shows
musicales ha visto en el último año y almacene ese número en una
variable. A continuación mostrar en pantalla un valor de verdad
(True o False) que indique si el usuario ha visto más de tres shows.
"""

# shows = int(input('Shows vistos en el último año: '))
# print(shows > 3)

""" Ejercicio 11
Escribí un programa que le solicite al usuario ingresar un facha 
formada por 8 números, donde los dos primeros representan el día, los
siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato
debe guardarse en una variable tipo int (número entero). Finalmente, 
mostrar al usuario la fecha con el formato DD / MM / AAAA 
"""

# fecha = int(input('Fecha en formato DDMMAAAA: '))
# fechat = str(fecha)
# print(f'{fechat[0:2]} / {fechat[2:4]} / {fechat[4:]}')

""" Ejercicio 12
Escribí un programa para solicitar al usuario el ingreso de un número
entero y que luego imprima un valor de verdad dependiendo de si el
número es par o no. Recordar que un número es par si el resto, al 
dividirlo por dos 2, es 0. 
"""

# num = int(input('Número entero: '))
# print(num % 2 == 0)

""" Ejercicio 13
Escribí un programa que solicite al usuario su edad y la guarde en una 
variable. Que luego solicite la cantidad de artículos comprados en 
una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla
un valor de verdad que indique si el usuario es mayor de 18 años de 
edad y ademas compró más de un artículo.
"""

# edad = int(input('Tu edad: '))
# art = int(input('Artículos comprados: '))
# print(edad > 17 and art > 1)

""" Ejercicio 14
Escribí un programa que, dada una cadena de texto por el usuario, 
imprima True si la cantidad de caracteres en la cadena es un
número impar, o False si no lo es.
"""

# cadena = input('Ingresá una frase: ')
# print(len(cadena) % 2 == 0)

""" Ejercicio 15
Escribí un programa que le pida al usuario ingresar dos palabras y las
guarde en dos variables, y luego imprima True si la primera palabra es 
menor que la segunda o False si no lo es.
"""

# cad1 = input('Una palabra: ')
# cad2 = input('Otra palabra: ')
# print(len(cad1) < len(cad2))

""" Ejercicio 16
Escribí un programa para pedir al usuario su nombre y luego el nombre
de otra persona, y almacenando cada nombre en una variable. Luego
mostrar en pantalla un valor de verdad que indique si: los nombres
de ambas personas comienzan con la misma letra ó si terminan con la 
misma letra. Por ejemplo, si los nombres ingresados son María y Marcos,
se mostrará True, ya que ambos comienzan con la misma letra. Si los 
nombres son Ricardo y Gonzalo se mostrará True, ya que ambos terminan 
con la misma letra. Si los nombres son Florencia y Lautaro se mostrará
False, ya que no coinciden ni la primera ni la última letra.
"""

# nom1 = input('Tu nombre: ')
# nom2 = input('Otro nombre: ')
# print((nom1[0] == nom2[0]) or (nom1[len(nom1)-1] == nom2[len(nom2)-1]))


""" Ejercicio 17
Escribí un programa que, dado un número entero, muestre su valor 
absoluto. Recordá que, para los números positivos su valor absoluto
es igual al número (el valor absoluto de 52 es 52), mientras que, 
para los negativos, su valor absoluto es el número multiplicado 
por -1 (el valor absoluto de -52 es 52).
"""

# num = int(input('Número: '))
# if num < 0:
#     num_abs = num * (-1)
# else:
#     num_abs = num
# print(f'Valor absoluto: {num_abs}')

""" Ejercicio 18
Escribí un programa que solicite al usuario el ingreso de dos números
diferentes y muestre en pantalla al mayor de los dos.
"""

# num1 = int(input('Un número: '))
# num2 = int(input('Otro número distinto: '))
# if num1 > num2:
#     print(f'{num1} es mayor')
# else:
#     print(f'{num2} es mayor')

""" Ejercicio 19
Escribí un programa que solicite al usuario una letra y, si es una vocal,
muestre el mensaje 'Es vocal'. Verificar si el usuario ingresó un string
de más de una carácter y en este caso, informarle que no se puede procesar
el dato.
"""

# letra = input('Letra: ')
# vocales = 'AEIOUaeiou'
# if len(letra) == 1:
#     for vocal in vocales:
#         if vocal == letra:
#             print('Es vocal')
#             break
# else:
#     print('No se puede procesar el dato')

""" Ejercicio 20
Escribí un programa para solicitar al usuario tres números y mostrar en 
pantalla al menor de los tres.
"""

# num1 = int(input('Primer número: '))
# num2 = int(input('Segundo número: '))
# num3 = int(input('Tercer número: '))
#
# if num1 < num2 and num1 < num3:
#     print(f'Menor: {num1}')
# elif num2 < num1 and num2 < num3:
#     print(f'Menor: {num2}')
# elif num3 < num2 and num3 < num1:
#     print(f'Menor: {num3}')

""" Ejercicio 21
Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
Si el nombre es 'Gwenevere' y la contraseña es 'excalibur', mostrar en pantalla
'Usuario y contraseña correctos. Puede ingresar a Camelot'. Si el nombre
o la contraseña no coinciden, mostrar 'Acceso denegado'.
"""

# nombre = input('Nombre de usuario: ')
# contra = input('Contraseña: ')
# n = 'Gwenevere'
# c = 'excalibur'
# if nombre == n and contra == c:
#     print('Usuario y contraseña correctos. Puede ingresar a Camelot')
# else:
#     print('Acceso denegado')

""" Ejercicio 22
Escribí un programa que permita saber si un año es bisiesto. Para que un
año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
excepto que también sea divisible por 400.
"""

# anio = int(input('Año: '))
# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print('Bisiesto')
# else:
#     print('No bisiesto')

""" Ejercicio 23
Escribí un programa que le solicite al usuario un número entero y muestre
todos los correlativos entre el 1 y el número ingresado por el usuario.
"""

# num = int(input('Ingresá un número: '))
# i = 1
# while i <= num:
#     print(i)
#     i += 1

""" Ejercicio 24
Escribí un programa que muestre la sumatoria de todos los numeros entre el 0
y el 100.
"""
# suma = 0
# for i in range(1, 100 + 1):
#     s = suma
#     suma += i
#     print(f'{s} + {i} = {suma}')

""" Ejercicio 25
Escribí un programa que, dado un número por el usuario, muestre todos sus 
divisores positivos. Recordá que un divisor es aquel que divide al número
de forma exacta (con resto 0).
"""

# num = int(input('Número: '))
# i = 1
# print('Divisores:')
# while i <= num:
#     if num % i == 0:
#         print(i)
#     i += 1

""" Ejercicio 26
Escribí un programa que, dada una frase por el usuario, muestre la cantidad total
de vocales (tanto mayúsculas como minúsculas) que contiene.
"""

# frase = input('Frase: ')
# vocales = 0
# v = 'AEIOUaeiou'
#
# for x in frase:
#     if x in v:
#         vocales += 1
#
# print(f'Vocales: {vocales}')

""" Ejercicio 27
Escribí un programa que muestre los primeros 10 números de la sucesión de
Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos,
cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1,
2, 3, 5, 8, 13, 21, 34, 55...
"""

fi_2 = 0
fi_1 = 1
fi = 0
print(0)
print(1)
for i in range(10):
    fi = fi_2 + fi_1
    fi_2 = fi_1
    fi_1 = fi
    print(fi)

""" Ejercicio 28
Escribí un programa que, dado un número entero positivo, calcule y muestre su
factorial. El factorial de un número se obtiene multiplicando todos los números
enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1. 
"""


# num = int(input('Ingrese un número positivo: '))
# factorial = 1
# i = 1
# while i <= num:
#     factorial *= i
#     i += 1
# print(f'Factorial: {factorial}')

""" Ejercicio 29
Escribí un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos.
Al final, mostrar la sumatoria de los números negativos y el promedio de los positivos. No olvides que 
no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se 
ingresaron números positivos.
"""

# sum_ = 0
# suma = 0
# np = 0
# for i in range(6):
#     num = int(input('Número: '))
#     if num < 0:
#         sum_ += num
#     if num > 0:
#         suma += num
#         np += 1
# print(f'Sumatoria de los negativos: {sum_}')
# if np > 0:
#     promedio = suma / np
#     print(f'Promedio de los positivos: {promedio}')

""" Ejercicio 30
Escribí un programa que permita al usuario ingresar una frase y luego un carácter
(string de longitud 1) y luego muestre la frase ingresada, pero con todas las ocurrencias del carácter
indicado por el usuario reemplazadas por "*".
"""

# frase = input('Frase: ')
# carac = input('Carácter: ')
# frase2 = ""
# for letra in frase:
#     if letra == carac:
#         frase2 = frase2 + "*"
#     else:
#         frase2 = frase2 + letra
# print(frase2)

""" Ejercicio 31
Escribí un programa que, dada una frase por el usuario, la muestre invertida, sin utilizar 
una rebanada con paso negativo
"""

# frase = input('Frase: ')
# frase2 = ''
# for letra in frase:
#     frase2 = letra + frase2
# print(frase2)

""" Ejercicio 32
Escribí un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
cortando el ingreso cuando el usuario el monto 0. Si ingresa un monto negativo, no se 
debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a 
pagar teniendo en cuenta que, si las ventas superan el monto total de 1000 se le debe aplicar 
un 10% de descuento.
"""

# numero = int(input('Monto: '))
# suma = 0
# while numero != 0:
#     if numero >= 0:
#         suma += numero
#     else:
#         print('Monto no válido.')
#     numero = int(input('Monto: '))
#
# if suma > 1000:
#     suma *= 0.9
# print(f'Monto total a pagar: {suma}')

""" Ejercicio 33
Escribí un programa que permita al usuario ingresar una cantidad de números
positivos indefinida (la cantidad que ingresará no se conoce y puede cambiar en cada 
ejecución), finalizando cuando ingresa el número 0 (que no tendrá en cuenta). Una vez terminada 
la lectura de números, informar cuál fue el mayor de los números ingresados.
"""

# numero = int(input('Número: '))
# max = -1
# while numero != 0:
#     if numero > 0:
#         if numero > max:
#             max = numero
#     else:
#         print('Número no valido.')
#     numero = int(input('Número: '))
# print(f'Mayor número ingresado: {max}')

""" Ejercicio 34
Escribí un programa que pregunte al usuario si desea analizar calificaciones de 
alumnos y, sólo si responde 'S' comenzará el procesamiento de los datos, hasta que el usuario ingrese
algo diferente de 'S'. Por cada alumno, permitir ingresar 
"""

