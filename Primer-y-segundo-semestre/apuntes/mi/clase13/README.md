# MySQL
## use
Nos permite posicionarnos en una base de datos
```sql
use <nombre de la base>;
```

## Cargar datos en las tablas 
Para cargar datos a nuestra tablas utilizaremos también una sentencia SQL propiamente del lenguaje a partir de palabras reservadas, en este caso utilizaremos:
```sql
insert into <nombre de la tabla> values (<valores>);
```
- Para tener en cuenta los datos en números se escriben en números.
- Los datos tipo carácter o varchar se escriben entre comillas simples 'Nombre'.

Una vez que utilizamos los comandos `insert into`con todos los valores de nuestra tabla, ejecutaremos con el botón del rayo.

## Sentencia `select`
La sentencia `select` es para mostrar, ver, visualizar datos de una base de datos.

### `select * from`
Utilizaremos la sentencia `select * from` para visualizar los datos ingresados en nuestra tabla, en este caso al ejecutar la sentencia utilizaremos el botón del rayo con el cursor, para ejecutar sólo la ultima línea.

```sql
select * from <nombre de la tabla>;
```

Una vez ejecutado el comando nos aparecerá la tabla con los datos ingresados.

### `select <columna> from <tabla>;`
Nos permite traer datos específicos cuando no utilizamos el asterisco y seleccionando sólo datos que necesitamos.
Podemos traer datos de diferentes columnas: 
```sql
select columna1, columna3, columna5 from base.tabla;
```


# Actividad 1
Generamos datos para nuestras tablas creadas en cada base de dato de la clase n° 12, añadiendo tres filas de datos cada una de ellas. 

> Utilizar las sentencias:
> - `use`
> - `insert into`
> - `select * from`