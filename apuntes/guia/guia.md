# Guía para conectar nuestra computadora con **Git Bash**

En esta guía vamos a ver como clonar un repositorio desde github.com, y 
también las configuraciones que debemos tener en cuenta para conectarnos.

## Configuración de cuenta github.com

Para este paso debemos tener lo siguientes datos:
- Usuario de **github.com**
- Mail con el que nos creamos la cuenta de **github.com**
- Contraseña de la cuenta que nos deseamos conectar

### Configuración del usuario

Usaremos el comando `git config` con la bandera `--global` para ingresar el nombre de usuario como la variable `user.name` de funcionamiento de **Git Bash**. Debemos ingresar el mismo nombre de usuario que tenemos en **github.com**

```bash
usuario@computadora MINGW64 ~
$ git config --global user.name "agustin1996ra"
```

### Configuración de mail

Utilizando el mismo comando con la misma bandera, pero la variable que modificaremos es `user.email`.

```bash
usuario@computadora MINGW64 ~
$ git config --global user.email "rodriguezalvarezagustin@gmail.com"
```

### Configuración de contraseña

## Subir un repositorio de **Git Bash** a **github.com**

Para poder conectarse a **github.com** con **Git Bash** se utiliza el protocolo SSH (Secure Shell), este es un protocolo criptográfico basado en el concepto de 'Llaves Publicas-Privadas'. En la actualiza no se permite el uso de contraseña de **github.com**.

Los sistemas de llaves publica-privada, funcionan utilizando algoritmos que encriptan diversos archivos que se enviaran por internet. 

Para utilizar el servicio de SSH tenemos que generar una llave SSH 


