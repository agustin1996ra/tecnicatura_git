# Clase 8: Comandos Git y ramas auxiliares

## Repaso de la clase anterior:
- Estuvimos viendo algunos comandos para abrir carpetas
- También algunas sintaxis de git
- Y ejercicios sobre los temas vistos
- Se nos dio una guía para descargar de comandos y su significado

## Recordatorio de temas vistos:

### Ramas:

Sabemos que al iniciar nuestro repositorio estaremos creando nuestra rama *master* o *main*. Cada commit en nuestra rama nos dirá las confirmaciones que añadiremos al mismo.

Por seguridad de nuestro proyecto siempre utilizaremos ramas auxiliares para evitar cualquier inconveniente en nuestra rama *main* y que esta de dañe.

### Comandos:

Para recordar cada vez que vamos a consultar cuantas ramas tenemos en nuestro proyecto, utilizaremos el comando.

```
usuario@computadora MINGW64 ~/repositorio (master)
$ git branch
```
```
usuario@computadora MINGW64 ~/repositorio (master)
$ 
```

Este comando nos permite ver las ramas creadas en el proyecto. Sólo aparecerá la rama *main* o *master* en caso de no haber creado ninguna rama hasta el momento.

### Espacio temporal 

Cuando hablamos de ramas tambien hacemos referencia a que va a ser un espacio temporal en el cual vamos a estar trabajando.

A medida que vamos avanzando en nuestro proyecto y hemos agregado las modificaciones necesarias al proyecto final, es aconsejable eliminar las ramas que ya no vamos a utilizar.

### Para movernos de una rama a otra

Los comandos:

```
usuario@computadora MINGW64 ~/repositorio (master)
$ git checkout "nombre de la rama"
```

```
usuario@computadora MINGW64 ~/repositorio (master)
$ git switch "nombre de la rama"
```

Son comandos que me permiten moverme de rama en rama o también una vez que cree una nueva rama y quiero regresar a la rama *main*, me permite volver a la rama principal.

> No olvidar que cada vez que creamos una nueva rama, nuestro puntero (head) se posicionará en la nueva rama.

### El orden de nuestros *commit*

Cada vez que vamos a realizar una *commit* en una rama, **Git** respetará el orden en el que hemos realizado dichas confirmaciones.

Si primero realizamos un *commit* en la rama *main* y luego confirmamos otros *commit* en la nueva rama, cuando digitemos el comando.

```
usuario@computadora MINGW64 ~/repositorio (master)
$ git log
```

Nos aparecerá el último *commit* primero en la lista y el primer *commit* al final de la lista.

### El comando log

Es un comando que voy a utilizar para ver el estado de mis *commit*.

Si añadimos 

```
usuario@computadora MINGW64 ~/repositorio (master)
$ git log --oneline --all
```

Podremos ver todas las ramas creadas y cada *commit* realizado en ellas.

# Actividades

## Actividad n°1

Responder el cuestionario para asistencia (aula del campus)

## Actividad n°2

1. Realizar la siguiente actividad evaluativa de manera grupal

    1. Crear un nuevo repositorio con el nombre clase8
    2. Crear tres carpetas: Martes, Miércoles y Jueves
    3. Guardar en cada carpeta documentos de texto.
    4. Realizar modificaciones, añadir los cambios y hacer *commit* utilizando cualquier editor de texto.

2. Crear tres ramas con sus *commit*

    1. Crear una nueva rama con el nombre de "Desarrollo".
    2. Crear una nueva carpeta con el nombre "Viernes" ubicados en la nueva rama.
    3. Añadir documentos de texto, modificar el documento y realizar los *commit* (5 modificaciones con sus *commit*).
    4. Mergear a la rama auxiliar a la rama *main*.
    5. Creamos una nueva rama con el nombre "Proceso".
    6. Aplicamos los pasos anteriores con una nueva carpeta que diga "Sábado" añadimos documento de texto, guardamos, añadimos, *commiteamos* (5 *commit*).
    7. Y por ultimo mergeamos a la rama *main*.
    8. Estando ubicados en la *main* creamos otra rama nueva con el nombre "tabla".
    9. Aplicamos los pasos realizados en las ramas anteriores y creamos una carpeta "Lunes", añadimos documentos de texto, guardamos, añadimos, hacemos 5 *commit* y mergeamos.

3. Eliminamos ramas auxiliares

    1. Eliminamos solo dos ramas auxiliares. Tener en cuenta que para eliminar las ramas auxiliares se debe estar ubicado en la rama *main*.
    2. Comprobar la cantidad de ramas que tiene nuestro proyecto una vez eliminada las dos ramas auxiliares.
    3. Enviar capturas con el nombre del grupo y de los integrantes (indique puntos trabajados en cada captura realizada) Formato pdf, word, PowerPoint, etc.


 

