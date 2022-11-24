# MySQL

# Sentencias 
## `order by`
Se utiliza para ordenar de forma ascendente o descendente un campo en una tabla, ya sea por medio de A a la Z, Z a la A de 1 hasta el infinito o desde el infinito hasta el 1.
### Orden ascendente
```sql
use base1;
select * from base1.tabla1 order by columna asc;
```
### Orden descendente
```sql
use base1;
select * from base1.tabla1 order by columna desc;
```
## Sentencia `not`
El operador `not` lo que hace es que no me muestra el valor que yo le indique, esto me permitirá traer sólo los datos que necesito trabajar en ese momento.

```sql
use base1;
select * from base1.tabla1 where not columna = "dato especifico";
```

## Sentencia `drop`
Esta sentencia nos permite eliminar columnas, un dato en específico y eliminar una base de datos.
```sql
Use base1;
alter table tabla1 drop column columna;
```
Se eliminará la columna seleccionada.

## Sentencia `delete`
Esta sentencia nos permitirá eliminar, contenidos de tablas específicas o en general.
Si utilizamos sólo el comando `delete from` y el nombre de la tabla eliminaremos todo el contenido de dicha tabla.

```sql
use base1;
delete from tabla1;
```

Para no eliminar todos los datos de una tabla acompañaremos el `delete` con el `where`

```sql
use base1;
delete from tabla1 where columna = "dato especifico";
```

De esta manera sólo estaríamos eliminando datos específicos y no todos los datos.

# Normalización 
La normalización es un proceso el cual los atributos  de una tabla pasan a ser re organizados, evitando así la repetición de estos y ahorrar espacio en una base de datos.

## ¿Para qué se utiliza?
La normalización es un proceso al cual el programador utiliza lo que es su lógica para evitar datos repetidos en una base de datos y así optimizar y ahorrar espacio y recursos en una empresa.

## Objetivo 

La normalización tiene como objetivo principal evitar la redundancia de datos en una base de datos y a su vez el ahorro de espacio en la misma. Muchas veces estarán limitados por la mismas empresas.

## Tres formas de normalización 
### Primera forma:
- Se encarga de eliminar los datos repetidos que tiene una tabla y separarlos.
- Crea una tabla por separado por cada grupo de datos relacionado.
- Identifica cada grupo de datos relacionados con una clave primaria.

### Segunda forma:
- Se crean tablas separadas para aquellos grupos de datos que se aplican a varios registros.
- Las tablas se relacionan mediante una clave externa.

### Tercera forma:
- Es la relación y dependencia que tiene cada tabla.
- Elimina todos aquellos campos que no dependan de una clave.

Por ejemplo, si la tabla A, B y C. B depende de A, entonces C depende de B y de A, pero si yo elimino B, C sigue dependiendo de A.

## Seleccionar datos de diferentes tablas
Utilizaremos el comando.
```sql
select * from tabla1, tabla2;
```

## Para seleccionar datos específicos de tablas
Utilizaremos
```sql
use base1;
select * from tabla1.columna2, tabla1.columna4, tabla2. n_tabla2 from usuario1, tabla2 where tabla1.columna1 = tabla2.columna1; 
```

# Actividad 
1. Responder cuestionario para asistencia en el campus.
2. Realizar ejercicios con sentencias vista durante la clase en las bases creadas en la clase anterior.

## Trabajo integrador grupal fecha de entrega 7/12
1. Añadir datos completando con 5 o 6 usuarios.
2. Crear una nueva tabla en la base1 con el nombre "serial", añadir dos columnas (id, n_serial)
3. Seleccionar datos de tabla usuario y serial, seleccionar sólo 2 datos de usuario y 1 de serial.
Enviar captura por grupo de lo realizado.