# Guía de comandos

## Comandos de Bash

### `mkdir`

Crea un directorio nuevo tomando en cuenta la ubicación actual.

### `pwd`

Nos muestra la carpeta actual en la que nos encontramos.

### `cat`

Nos permite ver el contenido de un archivo.

### `cd`

Nos permite cambiarnos de carpeta.

### `cd ..`

Nos llevara a la carpeta o directorio anterior.

### `cd -`

Nos llevara directamente al ultimo directorio visitado.

### `ls`

Nos mostrara los archivos de la carpeta donde estamos actualmente.

### `ls -l`

Ver todos los archivos como una lista donde se incluye la información del usuario, grupo, permiso sobre el archivo, tamaño y fecha y hora de creación.

# Comandos y ejercitación Git

Clase de repaso de comandos y ejercitación de clases vistas:

## Sintaxis de Git

El `~` es el ***path*** absoluto de (ruta) del usuario que estés usando, es decir la carpeta personal del usuario con el que estas logueado.

Por ejemplo, cuando entramos a la carpeta de nuestro usuario nos arroja nombre del usuario.

```
NombreUsuario@Computadora MINGW64 ~ 
$ 
```

## Guía de algunos comandos útiles 

- `pwd`: Nos muestra la carpeta actual en la que nos encontramos.
- `cat`: Nos permite ver el contenido de un archivo.
- `cd`: Nos permite cambiarnos de carpeta.
- `cd ..`: Nos permite regresar al directorio padre.
- `cd -`: Nos lleva directamente al ultimo directorio visitado.
- `ls`: Nos permite cel los archivos de la carpeta donde estamos actualmente.
- `ls -l`: Veremos todos los archivos como una lista en donde se incluye el usuario, grupo, permisos sobre el archivo, tamaño, fecha y hora de creación.
- `clear`: nos permite limpiar la pantalla.

## Comandos clase n°1

1. Crear la carpeta del repositorio:
    
    `mkdir`
2. Inicializar el repositorio:

    `git init`
3. Configuración de Usuario y Correo:

    `git config --local user.name "Nombre Usuario"`
    
    `git config --local user.email "usuario@ejemplo.com"`

## Comandos clase n°2

1. Creamos un archivo.
2. Guardamos el archivo en la carpeta dentro de las carpetas creadas en la 1ra. actividad.
3. Hacemos el `commit`.

```bash
$ git status
$ git add .
$ git commit -m "comentario del commit"
```


