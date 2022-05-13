# Clase 4

## Comandos que aprendimos en la clase anterior
- git commit -am "nota de nuestro cambio"
- git checkout "nombre de archivo"
- git checkout -f
- git restore --staged "nombre de archivo"
- git diff
- git diff --stat
- git diff --numstat

## Como cargar una version previa del repositorio?
Cada commit tiene un número de id o #

Con:

```commandline 
$ git checkout "número de identificación"
```

(del id de pueden copiar sólo los primeros 7 dígitos)

Podremos ver entonces a como estaba nuestro proyecto sin las modificaciones nuevas.

Para volver al presente donde esta mi último commit ejecutamos

```bash
$ git checkout master
```

Con el comando 

```bash
$ git log --oneline
```

obtendremos una lista de los commits hasta el momento, en la lista tendra como indice los 
primeros 7 caracteres del hash. 

ej:

```bash
rodri@laptop-agus MINGW64 ~/TecnicaturaGit/spd (master)
$ git log --oneline
c071838 (HEAD -> master) Commit de ejercicio como practica de la clase 4 de spd
b98f688 Elimine la carpeta nuevacarpeta, simplemente era de prueba.
3114029 Actualizacion de configuraciones
35d08d0 Correccion de las anotaciones
8cf9725 Cambio de nombre del proyecto para mayor consistencia
e3625a0 Avance de la clase4 de Programacion
253bd81 Avance de la clase4 de laboratorio
f5091a6 Avance de la clase4 de laboratorio
bb603f7 Avance de clase 4 de laboratorio
52c6b82 Avance de los proyectos de java y python
8520aa3 actualizamos readme.txt
13fa1fc Actividad realizada en la clase 3
683aa87 en este commit hicimos la prueba git add y git commit
4e2b8c4 no se que estoy haciendo
b97f0e7 Creamos el primer proyecto de Python La leccion 1
5cdd4a8 Iniciamos el proyecto de Java
ef5c4d0 Creamos los practiacas iniciales de python
```

Utilizando el comando: (siendo x el numero de commit)

$ git log --oneline -n x

veremos una lista de los ultimos x commit.


Entonces escribiendo el comando 

$ git checkout bb603f

EL nuevo commit HEAD seria "bb603f7 Avance de clase 4 de laboratorio",
osea las modificaciones en nuestro proyecto se verian tal cual como lo que 
incluimos en el commit bb603f7.

Para luego volver al ultimo commit se utiliza

$ git checkout master


## git log --raw
Este comando nos permite saber cuales fueron los cambios que pasaron en un 
commit.
Nos mostrará también que tipo de acciones hicimos si modificamos un archivo,
lo borramos o añadimos algo nuevo. Además nos muestra el código de seguridad
de nuestros commit.

## git log --pritty=format:" "
Este comando permite agregar el formato que se desee, por ejemplo:
el nombre del autor, correo, fecha, etc. A la lista que genera el comando 
"git log".
ej:

$ git log --pretty=format:"El autor del commit {%h} fue %an"


## Ramas
Dentro de mi rama (master) puedo crear ramas nuevas o auxiliares.
Esto nos indicará que vamos a tener varias lineas de tiempo con diferentes 
commit y diferentes periodos. Una linea de tiempo por cada rama.

Cada línea tiene su independencia y nuevas características, esto nos permite 
solucionar problemas que pueden surgir en la (master) y así evitar dañar nuestro
proyecto.

Podriamos tener un rama (master) donde identificamos errores o puntos de 
mantenimiento de nuestro proyecto, pero aun asi funciona. Entonces creamos 
una nueva rama de desarrollo donde podamos probar diferentes cambios en nuestro
proyecto de manera segura y cuando se compruebe la estabilidad de la nueva 
version, remplace a la rama (master) como la nueva version principal del
proyecto.

Para crear una nueva rama se utiliza el comando 

$ git checkout -b <nombre de la nueva rama>

Automaticamente nuestro puntero se movera a la rama nueva, para volver 
debemos utilizar el comando 

$ git checkout master #o el hash de otro commit en la rama principal 

En la nueva rama podremos realizar commit sin que alteren el estado 
de la rama principal.



El comando:

$ git branch

nos permite ver las ramas del repositorio, marcando donde tenemos el puntero
con un * y en git bash con color


El comando 

$ git log --oneline --all --graph --decorate

nos mostrara de manera un poco mas grafica los diferentes commit
de nuestas ramas, marcando con una indexacion las diferentes ramas,
programe un alias llamado "decobranch" en git bash.



