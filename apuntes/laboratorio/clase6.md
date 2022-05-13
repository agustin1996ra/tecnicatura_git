# Clase 6

### Evaluacion del primer semestre
Los temas de la evaluacion seran los temas de Fundamenteos de la programación.

Todos los grupos que hayan presentado sus proyectos:
- Hecho y explicado por todos los miemobros del grupo
- Hacer un video como grupo, para presentarlo en el canal.
	- Explicar el proyecto presentado de manera mas extensa (no mas de 30min)
	- Ejercicio y documentacion
	- Participar todos los miembros
	- Con imagenes
	- Sin datos personales
	- Iniciales del nombre y apellido completo
Sera para hacer un cierre del primer semestre de todas las materias
- agreagar capturas de pantallas de nuestro ordenadores con los trabajo hechos
de cada una de las catedras
- Esto sera el cierre del primer semestre

Aquellas personas que no particepen en los videos, deberan participar en una
llamada de zoom con todos los docentes para evaluar el desempeño en cada 
una de las catedras en el primer semestre

## Temas de la clase

### Fundamentos de la programacion
- Variables
- estructuras de datos
- los tipos de datos 
- que es un objeto 
- o un funcion
- los condicionales
- los ciclos

Estos conceptos basicos se aplican a todos los lenguajes, una vez los entendes
ya no te complicaras en cada lenguaje.

### Primer lenguaje

despues de aprender los fundamentos de programacion, podras elejir tu primer amor.
por donde empezar: Python, Java, Go y JavaScript

#### Python 
Es el lenguaje mas usado en el mundo y el n°1 en inteligencia artificial y 
ciencia de datos, que son áreas con mucho crecimiento en los ultimos años.
Tiene otras areas como el desrrollo web y la seguridad informatica 

#### JAVA
Este lenguaje brilla en el backend y los microservicios, aunque puede utilizarse
en otros ambitos, como programas de escritorio, desarrollo movol, sistemas 
embebidos, etc. Las grandes empresas usan JAVA para todos sus sistemas por lo
que nunca te faltarán oportunidades laborales. Además, es un lenguaje solido que
esta todos los años en el tpo 5 de los mas utilizados.

#### Go
Igual que JAVA, brilla en el backend y los microservicios. Muchos programadores
de JAVA se estan moviendo a Go porque es más sencillo de implementar, es menos
verboso y tiene mejoras en las interfaces, en la concurrecia y además, hacer un
deploy es Go es muy sencillo mientras que en JAVA es muy complejo. Asimismo, muchas
empresas estan mudando su backend a Go, por lo qué, actualmente, hay más demanda
que oferta y eso hace que los sueldos suban.

#### JavaScript
Es el lenguaje numero 1 de la web y uno de los mas usados del mundo. Duarante
casi una decada fue el más usado hasta que lo remplazó Python por la inteligencia
artificial que está creciendo mucho. JavaScript es Web, aunque tambien puedes 
hacer programas de escritorio, apps moviles, incluso machine lerning o realidad
virtual. Es un lenguaje muy versatil y en la web, es el campo de programacion.

### Logica del programador


### Algoritmos


### Sentecias de Control

#### `if/else`
Generalmente la sentencia if else nos lleva a seleccionar un camino u otro.

Podemos observar el algoritmo, en la condicion debemos saber que lleva una 
expresion booleana donde tenemos el valor Verdadero o Falso, solo es uno de los 
caminos.

Un dato importante:
La identacion solo necesita un espacio, el tabulador agrega por defecto cuatro.

La unica sentencia obligatoria es la `if`, no así el `elif` y el `else`, ya que 
estas quedan al uso y criterio del programador, según el uso que le quiera dar
al algoritmo.

##### Ejemplo:

```python
condicion = True
if condicion is True:
    print('Condición verdadera')
elif condicion is False:
    print('Condición Falsa')
else:
    print("Condición sin especificar")

```

### Ejecicio 1:

Escribir la siguiente expresión en fomra de expresión algorítmica.

((a**3)*((b**2)-(2*a*c))/(2*b)

1. Pedimos al usuario 3 valores = a, b, c
2. Mostramos el resultado final
 
Resolucion: /TecnicaturaGit/Python/leccion2

```python
a = float(input('Digite el valor de a: '))
b = float(input('Digite el valor de b: '))
c = float(input('Digite el valor de c: '))
resultado = ((a ** 3)*((b ** 2)-(2 * a * c)))/(2 * b)
print(f'El resultado es: {resultado}')
```

### Operador Ternario (sintaxis)

```python
condicion = True
print('Condición Verdadera') if condicion else print('Condición Falsa')
```
El operador ternario solo debe utilizarce en caso de que sea una accion muy simple
por que si no, este no podra cuplir con la tarea. Nunca se podra usar un elif.


### Ejercicio 2

Determinar la solución lógica de la siguiente opereación

```python

a = int(input('Digite un valor entero: a = '))
b = int(input('Digite un valor entero: b = '))
resultado = (((3 + 5 * 8) < 3) and ((((-6 / 3) * 4) + 2) < 2)) or (a > b)
print(f'El resultado de la operación es: {resultado}'

```

```commandline

Digite un valor entero: a = 2
Digite un valor entero: b = 4
El resultado de la operación es: False

```
### Ejercicio 3

Intercambiar el valor de dos variables

Por ej:
a = 10  ->  a = 5
b = 5   ->  b = 10

```commandline

Digite un valor entero: a = 4
Digite un valor entero: b = 2
El resultado de la operación es: True

```

### Ejercicio 4 

#### Área y longitud de un circulo

Hacer un programa para ingresar el radio de un círculo y se reporte su área
y el perimetro de la circunferencia.

```python
import math

r = float(input('Ingrese el radio de una circunferencia: r = '))
area = math.pi * (r ** 2)
perimetro = 2 * math.pi * r
print(f'Un circulo de radio = {r} , tiene un area = {area} y un perimetro = {perimetro} ')
```
