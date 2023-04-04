# MySQL - Sentencias

## Sentencias para traer datos específicos de una o varias tablas
Para ello utilizaremos las sentencias
```sql
use base1;
select * from tabla1 where columna like "J%";
```

El símbolo `%`, hace referencia a cuando buscamos un dato que empiece con una letra, se va a colocar la letra especifica de la búsqueda y luego el signo de porcentaje.

`letra%`

Si se quiere buscar una palabra que finalice con una determinada letra se colocará delate de la letra.

`%letra`

O si se necesita buscar datos que contengan letras específicas se colocará.

`%letra%`

También se puede especificar por cantidad de caracteres que tenga un dato.
Según la cantidad de caracteres que tenga ese dato.
Por ejemplo si un dato tiene 5 caracteres utilizaremos el guión bajo "_" según la cantidad de caracteres que necesitamos que nos arroje.

```sql
use base1;
select * from tabla1 where columna like "_____";
```

## Como cambiar nombre de columnas y tablas utilizando sentencias

Para cambiar el nombre a las columnas utilizaremos.
