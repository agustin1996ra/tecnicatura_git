# MySQL
## Lenguaje SQL
Los origenes del SQL nos llevan a la década de 1970, cuando en IBM se creó un software de base de datos, llamada System R. Para gestionar los datos almacenados en System R se creó el lenguaje SQL.

## SQL
Es un lenguaje que nos permite maniobrar, crear, modificar y gestionar bases de datos. En ese entonces no se las mencionaba como base de datos, sino como base de almacenamiento.

Es un lenguaje de computación para trabajar con un conjunto de datos y las relaciones entre ellos.

## Que nos permite?
Cuando nosotros hablamos de SQL nos estamos refiriendo a algo relacional. 

Al ser un modelo relacional, necesitamos entidades, tablas, columnas.

Necesitamos que todo tenga relación entre si, que la información tenga sentido en conjunto y no por separado.

## Para que se utiliza?
SQL se utiliza para describir conjuntos de datos que pueden ayudarte a responder preguntas.

Al usar ese lenguaje se debe usar la sintaxis correcta.

## Sintaxis
Sintaxis en la forma en que se escribe un comando. Son las reglas que deben seguir para dar órdenes.

La sintaxis SQL se basa en la sintaxis del idioma inglés y usa mucho de los mismo elementos de Visual Basic.

## Elemento SQL

### Línea de comandos 
Todos los comandos necesarios en los sistemas de gestión se ejecutan a través de una interfaz especifica llamada línea de comandos SQL (Command-line interface o CLI).

### Querys (consulta)
Es una sentencia que va a dar una orden o una indicación.

Va a recuperar los datos en base a un criterio dado, trayendo datos de una base de datos o de una tabla.

### Cláusulas SQL

Son también sentencias que nos da estados de cada uno de los componentes de la base de datos y de cómo están las querys, si se ejecutan o si no se ejecuta.

Todas las cláusulas van a realizar siempre una función.

Se ve error de sintaxis, entre otras cosas.

Cláusulas | Descripción
----|----
FROM | Utilizada para especificar la tabla de la cual se van a seleccionar los registros.
WHERE | Utilizada para especificar las condiciones que deben reunir los registros que se van a seleccionar.
GROUP BY | Utilizada para separar los registros seleccionados en grupos específicos.
HAVING | Utilizada para expresar la condición que debe satisfacer cada grupo.
ORDER BY | Utilizada para ordenar los registros seleccionados de acuerdo con un orden específico.

### Comandos (sentencias)
Se utilizan para el envío de consultas desde un programa cliente a un servidor donde se almacenan las base de datos.

Un comando es una sentencia u orden, es una indicación que se le da a partir de una nomeclatura propia de SQL.

## Tipos de comandos 
Existen dos tipos de comandos SQL:

- DDL
- DML

### DDL (Data Definition Languaje)
Nos va a permitir crear nuevas bases de datos, campos e índices.

Un campo es un espacio en el que va a ir un dato, mientras que un índice es un espacio donde se va a agrupar un dato.

Estos tres comandos son:
- Create
- Drop
- Alter

#### Comandos DDL

Create: Sirve para eso, para crear nuevos campos, ya sean nuevas bases de datos, nuevas tablas, nuevos campos, nuevos índices.

Drop: Sirve para eliminar tablas e índices.

Alter: es utilizado para modificar las tablas agregando campos o cambiando la definición de los mismos.

### DML (Data Manipulation Languaje)
Su función es la manipulación de Datos, a través de él podemos insertar, eliminar y actualizar datos.

También generar consultas para ordenar, filtrar y extraer datos de la base de datos.

#### Comandos DML
Insert: Es utilizado para cargar lotes de datos de una base de datos en una única operación. Un insert ca introducir nuevos datos o conjuntos de éstos en una base de datos (tabla).

Update: Utilizando para modificar los valores de los campos y registros especificados.

Delete: Utilizando para eliminar registros de una tabla de base de datos. Trabaja eliminando uno a uno los registros.

## Expresiones
Las expresiones pueden producir valores escalares o tablas que consisten en columnas y filas de datos.

Una expresión me va a tener como resultado distintas funciones, pero entre ellas la creación de columnas y tablas.

## Predicados
Los predicados especifican las condiciones que se utilizan para limitar los efectos de los comandos y las consultas o para cambiar el flujo del programa.

Un predicado ca a ser como un condicional que técnicamente le va a dar un alcance a un comando.

## Instancia:
Nos permite conectarnos a una base de Datos.

En Workbench vamos a crear una nueva instancia, haciendo click en el signo +, donde se nos abrirá una nueva ventana.

Escribimos el nombre de ka conexión en este caso colocaremos "Metodología" y hacer click en el botón Test connection, les pedirá la clave cuando abrieron Workbench, introducen la clave y luego dan ok y listo.

Se ha creado una nueva conexión

Ingresar a la nueva conexión creada.

Creamos una base de datos desde la ventana de comandos con el comando:
`create database <nombre de la base de datos>`

Hacemos click en el icono del rayo y automáticamente nos aparecerá debajo la confirmación que la base de datos ha sido creada.

Si refrescamos la información nos aparecerá la base de datos creada.

Creamos 2 base de datos más.

Creamos una tabla pero desde la ventana de comandos utilizando el siguiente comando:
```sql
use base1;
create table usuario(
    id int(2) primary key,
    nombre varchar(50),
    apellido varchar(50),
    correo varchar(100));
```

Ejecutamos con el botón del rayo, refrescamos y veremos como aparece la tabla creada.

# Actividad
1. Realizar cuestionario para la asistencia en el campus de 21 a 23hs.
2. Crear una nueva conexión con el nombre "Metodología"
3. Crear una base de datos con el nombre "base1" desde la ventana de comandos.
4. Creamos dos base de datos más (en total debe haber 3 base de datos)
5. Dentro de cada base de datos ingresamos los comandos para crear una tabla.