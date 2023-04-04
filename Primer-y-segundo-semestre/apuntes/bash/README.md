# Comandos de Bash
 
## Lista de contenidos

> ## [Los basicos](#losbasicos-id) 
>
> ### [Primeros comandos, navegacion del sistema de archivos](#primeroscomandos-id)
>
> - [`pwd / ls / cd`](#pwdlscd-id)
> - [`; / && / &`](#cadenas-id)
>
> ### [Conseguir ayuda (help)](#ayuda-id)
>
> - [`-h`](#help-id)
> - [`man`](#manual-id)	
>
> ### [Ver y editar archivos](#vereditar-id)
>
> - [`head / tail / cat / less`](#headtail-id)
> - [`nano / nedit`](#nano-id)
>
> ### [Crear y eliminar archivos y carpetas](#crear-id)
>
> - [`touch`]()
> - [`mkdir / rm / rmdir`]()
>
> ### Mover y copiar archivos, crear links, historial de comandos
>
> - [`mv / cp / ln`]()
> - [Historial de comandos]()
>
> ### Arboles de directorios, uso del disco y procesos
>
> - [`mkdir -p / tree`]()
> - [`df / du / ps`]()
>
> ### Micelaneos
>
> - [`passwd / logout / exit`]()
> - [`clear / *`]()
>
> ## Intermedio

 

## Los basicos {#losbasicos-id}

### Primeros comandos, navegacion en el sistema de archivos {#primeroscomandos-id}

   Los sistemas de archivos modernos tienen arboles de carpetas, donde hay una
 carperta que es raiz (root) osea no esta contenida en una carpeta padre 
 (parent directory), y hay sub-carpetas (subdirectory) que estan contenidas
 por una unica carpeta llamada carpeta padre (parent).
   Recorriendo hacia atras atravez del arbol de carpetas (desde las carpetas
 hijo hacia las carpetas padre) siempre lo llevara hacia la carpeta raiz. Como en 
 Windows nos llevara a C:\ o D:\ segun en el disco que tengamos selecionado,
 en linux nos llevara a un unica carpeta raiz llamada /.

#### `pwd / ls / cd` {#pwdlscd-id}
Al usar un sistema de archivos el usuario siempre estara trabajando en alguna
carpeta en especifica, a la que se le llama "current directory" o "the 
working directory" (carpeta actual o carpeta de trabajo).

Para ver la ruta actual en la que estamos trabajando debemos usar:

```bash	
usuario@computadora:~ pwd
/home/usuario   # en linux
/c/Users/usuario  #en windows
```

Para ver la lista de las carpetas y archivos contenidos en la carpeta actual

```bash	
usuario@computadora:~$ ls
Documentos  notasAgus 
```	

Mostrara lo gen contenga la carpeta actual, si esta esta vacia no habra nada
que listar.


Para ver todas las carpetas y archivos incluyendo a los ocultos

```bash	
usuario@computadora:~$ ls -a
.              .bashrc     .landscape   .profile                   Documentos
..             .config     .local       .python_history            notasAgus
.bash_history  .gitconfig  .motd_shown  .sudo_as_admin_successful
.bash_logout   .java       .nedit       .viminfo
```	

Para ver las carpetas y archivos con detalle

```bash
usuario@computadora:~$ ls -l
total 8
drwxr-xr-x 2 agus_ra agus_ra 4096 May  9 07:54 Documentos
drwxr-xr-x 4 agus_ra agus_ra 4096 May 10 00:29 notasAgus
```

Se pueden utilizar multiples banderas

```bash
usuario@computadora:~$ ls -l -a
total 68
drwxr-xr-x 9 agus_ra agus_ra 4096 May  9 21:54 .
drwxr-xr-x 3 root    root    4096 Apr 28 07:40 ..
-rw------- 1 agus_ra agus_ra 3735 May  9 22:33 .bash_history
-rw-r--r-- 1 agus_ra agus_ra  220 Apr 28 07:40 .bash_logout
-rw-r--r-- 1 agus_ra agus_ra 4140 May  4 14:50 .bashrc
drwx------ 4 agus_ra agus_ra 4096 May  4 19:42 .config
-rw-r--r-- 1 agus_ra agus_ra   84 May  5 06:51 .gitconfig
drwxr-xr-x 3 agus_ra agus_ra 4096 May  9 21:54 .java
drwxr-xr-x 2 agus_ra agus_ra 4096 Apr 28 07:40 .landscape
drwxr-xr-x 3 agus_ra agus_ra 4096 Apr 28 07:57 .local
-rw-r--r-- 1 agus_ra agus_ra    0 May 10 00:10 .motd_shown
drwxr-xr-x 2 agus_ra agus_ra 4096 May  4 19:33 .nedit
-rw-r--r-- 1 agus_ra agus_ra  807 Apr 28 07:40 .profile
-rw------- 1 agus_ra agus_ra   72 May  8 06:57 .python_history
-rw-r--r-- 1 agus_ra agus_ra    0 Apr 28 07:51 .sudo_as_admin_successful
-rw------- 1 agus_ra agus_ra 2342 May  6 06:07 .viminfo
drwxr-xr-x 2 agus_ra agus_ra 4096 May  9 07:54 Documentos
drwxr-xr-x 4 agus_ra agus_ra 4096 May 10 00:29 notasAgus
```

Y en algunos casos se pueden combinar (rara vez entiendo)

```bash
usuario@computadora:~$ ls -la
total 68
drwxr-xr-x 9 agus_ra agus_ra 4096 May  9 21:54 .
drwxr-xr-x 3 root    root    4096 Apr 28 07:40 ..
-rw------- 1 agus_ra agus_ra 3735 May  9 22:33 .bash_history
-rw-r--r-- 1 agus_ra agus_ra  220 Apr 28 07:40 .bash_logout
-rw-r--r-- 1 agus_ra agus_ra 4140 May  4 14:50 .bashrc
drwx------ 4 agus_ra agus_ra 4096 May  4 19:42 .config
-rw-r--r-- 1 agus_ra agus_ra   84 May  5 06:51 .gitconfig
drwxr-xr-x 3 agus_ra agus_ra 4096 May  9 21:54 .java
drwxr-xr-x 2 agus_ra agus_ra 4096 Apr 28 07:40 .landscape
drwxr-xr-x 3 agus_ra agus_ra 4096 Apr 28 07:57 .local
-rw-r--r-- 1 agus_ra agus_ra    0 May 10 00:10 .motd_shown
drwxr-xr-x 2 agus_ra agus_ra 4096 May  4 19:33 .nedit
-rw-r--r-- 1 agus_ra agus_ra  807 Apr 28 07:40 .profile
-rw------- 1 agus_ra agus_ra   72 May  8 06:57 .python_history
-rw-r--r-- 1 agus_ra agus_ra    0 Apr 28 07:51 .sudo_as_admin_successful
-rw------- 1 agus_ra agus_ra 2342 May  6 06:07 .viminfo
drwxr-xr-x 2 agus_ra agus_ra 4096 May  9 07:54 Documentos
drwxr-xr-x 4 agus_ra agus_ra 4096 May 10 00:29 notasAgus
```

Para cambiar a una carpeta diferente 

```bash
usuario@computadora:~$ cd /mnt/c/Users/ususario/Escritorio
usuario@computadora:/mnt/c/Users/usuario/Escritorio$
```

Para ir a la carpeta padre (parent directory)

```bash
usuario@computadora:~$ cd ..
usuario@computadora:/home$
```

#### `; / && / &` {#cadenas-id}

Las cosas que escribimos en la consola o terminal son llamados comandos, estos
siempre ejecutan codigo almacendado en alguna parte de tu computadora. A veces
este leguaje de computadora es un comando preensamblado de linux, a veces es una
aplicacion, a veces será codigo escrito por vos. Ocacionalmente podemos 
necesitar ejecutar comandos uno detras de otro. Para hacer eso usaremos ; (punto
y coma).

```bash
usuario@computadora:~$ ls; pwd
bash.txt
/home/usuario
```

En el caso de arriba, el punto y coma dice, primero ejecuto ls y se lista el 
contenido de la carpeta, y despues ejecuto pwd y se muestra la ruta de la 
carpeta actual.

Otra herramienta para encadenar comandos es &&. Con &&, el comando de la 
derecha no se ejecutara si el de la izquierda falla. ; y && pueden ser 
utilizados muchas veces en la misma linea.

```bash
usuario@computadora:~$ cd notasAgus && pwd && ls 
/home/agus_ra/notasAgus
bash.md
```

En el caso de ; el comando de la derecha se ejecutara sin importar, si el 
comando de la izquierda se ejecuto correctamente.


& se ve similar a && pero en realidad ejecuta una funcion completamente
diferente. Normalmente, cuando ejecutas un comando de larga ejecucion, la linea
de comandos esperara hasta que ese comando termine, antes de que te permita
ejecuatar otro nuevo. Al poner & despues de un comando previene de que pase esto,
y te permite ejecutar un nuevo comando mientras el anterior se sigue ejecutando.

```bash
usuario@computadora:~$ cd notasAgus/ && mnv package &
```

Cuando usamos & despues de un comando para "ocultarlo", decimos que ese 
proceso esta "ejecutado en segundo plano". Para ver los procesos que estan
actualmete ejecutandose en segundo plano usamos el comando jobs.

```	
usuario@computadora:~$ jobs
[1]+ Running cd notasAgus/ && mnv package &
```	

### Conseguir ayuda (help) {#ayuda-id}


#### `-h` {#help-id}
Escriba -h o --help despues de la mayoria de comandos para traer el menu de ayuda
para ese comando.

```bash
usuario@computadora:~$ du --helpUsage: du [OPTION]... [FILE]...
  or:  du [OPTION]... --files0-from=F
Summarize disk usage of the set of FILEs, recursively for directories.

Mandatory arguments to long options are mandatory for short options too.
  -0, --null            end each output line with NUL, not newline
  -a, --all             write counts for all files, not just directories
      --apparent-size   print apparent sizes, rather than disk usage; although
                          the apparent size is usually smaller, it may be
                          larger due to holes in ('sparse') files, internal
                          fragmentation, indirect blocks, and the like
  -B, --block-size=SIZE  scale sizes by SIZE before printing them; e.g.,
                           '-BM' prints sizes in units of 1,048,576 bytes;
                           see SIZE format below

...
```

#### `man` {#manual-id}
Escriba man antes de la mayoria de comandos para traer el manual para ese comando
(para cerrar el manual oprima q)

```bash
usuario@computadora:~$ man du

DU(1)                             User Commands                            DU(1)

NAME
       du - estimate file space usage

SYNOPSIS
       du [OPTION]... [FILE]...
       du [OPTION]... --files0-from=F

DESCRIPTION
       Summarize disk usage of the set of FILEs, recursively for directories.
       Mandatory arguments to long options are mandatory for short options too.

       -0, --null
              end each output line with NUL, not newline

       -a, --all
              write counts for all files, not just directories

       --apparent-size

...
```

### Ver y editar archivos {#vereditar-id}

#### `head / tail / cat / less` {#headtail-id}

`head` genera una salida con las primeras lineas de una archivo(por defecto 10 linas)
Para especificar cuantas lineas se utiliza la bandera -n.

```bash
usuario@computadora:~$ head -n 5 notasAgus/bash.md
 
# Comandos de Bash
 
## Lista de contenidos
```


`tail` muestra las ultimas lineas de un archivo. Podes obtener las ultimas n
lineas como con head, o podes el final del archivo empezando desde la linea 
numero x con `tail -n +x` 

```bash
usuario@computadora:~$ tail -n +100 notasAgus/bash.md
De necesitar ejecutar comandos uno detras de otro. Para hacer eso usaremos ; (punto
y coma).

usuario@computadora:~$ ls; pwd
bash.txt
/home/usuario
```
En el caso de arriba, el punto y coma dice, primero ejecuto ls y se lista el
contenido de la carpeta, y despues ejecuto pwd y se muestra la ruta de la
carpeta actual.

Otra herramienta para encadenar comandos es &&. Con &&, el comando de la
derecha no se ejecutara si el de la izquierda falla. ; y && pueden ser
utilizados muchas veces en la misma linea.

```bash
usuario@computadora:~$ cd notasAgus && pwd && ls
/home/agus_ra/notasAgus
bash.md
```

En el caso de ; el comando de la derecha se ejecutara sin importar, si el
comando de la izquierda se ejecuto correctamente.


`cat` concatena una lista de archivos y lo envia por la salida estandar
(usualmente por la terminal). `cat` puede ser utilizado para un solo archivo,
o multiples archivos y es utilizado para verlos rapidamente.(**Este advertido**:
si usted utiliza `cat` de esta forma, puede ser acusado de Useless Use of
Cat (UUOC) / Uso inecesario de Cat, pero no es tan importante, asi que no te 
precupes mucho.)

```bash
usuario@computadora:~$ cat notasAgus/bash.md
bash.md (completo)
```
 
`less` es otra herramienta para rapidamente ver un archivo abre un ventana
tipo vim solo de lectura.( Sí, hay un comando llamado more, pero less anti 
intuitivamente ofrece un super set de funcionalidades de `more` y es recomendado
por sobre el)

#### `nano / nedit` {#nano-id}

`nano` es un editor de texto de la linea de comandos minimalista. Es un gran editor
para principiantes o para gente que no quiera aprenderce un millon de atajos de
teclado. (el autor del articulo dice que fue mas que suficiente para el  en los 
primeros años de la carrera de programador y que ahora esta trabajando con otros
mas potentes porque definir por uno mismo el resaltado de sintaxis en nano puede
ser doloroso.)

`nedit` es un editor de texto pequeño, se abre en una ventana y permite usar el 
raton para editar, arrastrar y soltar, tiene resaltado de sintaxis y mas.

Otros editores comunes CLI (command-line interface) / GUI (graphical
user interface) incluidos `emacs`, `vi`, `vim`, `gedit`, Notepad++, Atom y otros
mas. Algunos interesantes son Micro, Light Table y VS Code.

Todos los editores ofrecen caracteristicas basicas como buscar y remplazar,
resaltado de sintaxis, etc. `vi` and `emacs` tienen mas caracteristicas que 
`nano` y `nedit`, pero tienen una curva de apredizaje muy abrupta. Proba diferentes
editores y encontra el que funcione con vos.

### Crear y eliminar archivos y carpetas {#crear-id}

#### `touch` {#touch-id}

`touch` fue creado para modificar marcas de fecha, pero tambien puede ser usado 
para crear rapidamente archivos vacios. Podes crear un archivo nuevo abriendolo
con un editro de texto, como `nano`.

```bash
usuario@computadora:~$ touch readme.txt && ls
notasAgus	readme.txt
```

O con `nano`

```
usuario@computadora:~$ nano readme.txt
```

Se abrira el programa nano para editar el archivo readme.txt, y si guardamos 
el archivo se podra acceder a el.

LLevar a segundo plano nano, mientras se esta editando con ^z (Ctrl + z), con 
este atajo volveremos a la consola.

Luego podemos volver al proceso de nano con el comando fg.

```
usuario@computadora:~$ fg
```

Si queremos terminar el proceso alctual en primer plano podemos hacerlo
con ^c (Ctrl + c).

Si queremos terminar un proceso que se encuentra ejecutandose en segunso plano
podemos hacerlo con `kill %N` siendo N el indice del proceso mostrado por el
comando `jobs`.

#### `mkdir / rm / rmdir` {#mkdir-id}

`mkdir` se utiliza para crear carpetas nuevas.

```
usuario@computadora:~$ ls && mkdir nuevaCarpeta && ls
notasAgus	readme.txt	
notasAgus	nuevaCarpeta	readme.txt
```

Podes eliminar cualquier archivo con `rm`, pero cuidado por que no es recuperable

```bash
usuario@computadora:~$ ls && rm readme.txt && ls
notasAgus	nuevaCarpeta	readme.txt
notasAgus	nuevaCarpeta
```

Para eliminar una carpeta vacia utilizar `rmdir`. Si ejecutas `ls -a` en una
carpeta vacia, solo deberias ver la referencia a la carpeta en si (.) y la
referencia a la carpeta padre (..)

```bash
usuario@computadora:~$ ls && rmdir nuevaCarpeta && ls 
notasAgus	nuevaCarpeta
notasAgus
```
`rmdir` elimina carpetas vacias solamente:

```bash
usuario@computadora:~$ rmdir notasAgus
rmdir: failed to remove 'notasAgus/': Directory not empty
```

Pero podes eliminar una carpeta y todos sus contenidos con `rm -rf` 
(`-r` = recursive, `-f` = force)

```bash
usuario@computadora:~$ rm -rf notasAgus
```

###  Mover y copiar archivos, crear links, historial de comandos

#### `mv / cp / ln`

`mv` mueve y renombra archivos. Usted puede mover el archivo a una nueva carpeta,
y concervar el nombre que traia, o puede renombrar el archivos en la misma 
carpeta.

```bash
usuario@computadora:~$ ls && mv notasAgus/bash.md bash.md && ls
notasAgus
bash.md		notasAgus
```

`cp` copia los archivos

```bash
usuario@computadora:~$ ls && cp bash.md bash2.md && ls
bash.md 	notasAgus
bash.md	 	bash2.md	notasAgus
```

`ln` crea un hard link al archivo

```bash
usuario@computadora:~$ ln bash.md bash3.md
```

`ln -s` crea un soft link al archivo

```bash
usuario@computadora:~$ ln -s bash.md bash4.md
```

Un hard link referencia a los mismos bytes de memoria que contienen al archivo,
en cambion un soft link refiere al nombre del archivo original, que es referencia
a los bytes en memoria.

#### Historial de comandos

`bash` tiene dos caracteristicas principales para ayudarlo a completar y re
ejecutar comandos, la priemra es tab completion. Simplemente tipee la primera
parte de un comando, y oprima tab, y deje que la terminal adivine que esta 
queriendo hacer.

```bash
usuario@computadora:~$ ls (ENTER)
bash.md 	notasAgus

usuario@computadora:~$ ls n (TAB)
```

... apretando la tecla TAB despues de tipeear la letra n, el comando se completara

```bash
usuario@computadora:~$ ls notasAgus (ENTER)
bash.md
```

En caso de que haya una ambiguedad debera apretar TAB multiples veces.

`bash` conserva un breve historial de los comandos que usted ha tipeado
previamente y le permite buscar en los comandos al apretar ^r (ctrl + r)

```bash
usuario@computadora:~$ 
```

Oprima ^r para buscar en el historial de comandos

```bash
(reverse-i-search)`':
```

Eacriba una cadena de caracteres que se encuantre en el comando que esta buscando

```bash
(reverse-i-search)`com': git commit
```

### Arboles de directorios, uso del disco y procesos

#### `mkdir -p / tree`

`mkdir` por default solo crea una sola carpeta. Lo que significa que si la 
carpeta d/e no existe, no se puede crear la carpeta d/e/f con `mkdir`.


Pero si le ponemos la bandera `-p` a `mkdir`, este creara todas las carpetas 
en el path si es que estas no existen.


`tree` puede ayudarlo a visualizar mejor la estrictura de carpetas, al imprimir
con un formato lindo el arbol de carpetas. Por defecto, imprimira toda la 
estructura del arbol de carpetas, empezando con la especificada. Pero se puede
restrigir hasta un cierto numero de niveles con la bandera -L:

```bash
usuario@computadora:~$ tree -L 2
.
├── Documentos
└── notasAgus
    ├── bash.html
    ├── bash.md
    ├── bash.pdf
    └── img

3 directories, 3 files
```

Se puede ocultar las carpetas ocultas con la bandera --prune. Nota: esta bandera
tambien oculta carpetas 'revursivamente vacias', son carpetas que no esta vacias
por que contienen otras carpetas, pero que a su vez estas estan vacias o contienen
carpetas vacias.



#### `df / du / ps`

`df` es usado para mostrar el espacio ocupado por los archivos en tus dicos o 
sistema de almacenamiento.

```bash
usuario@computadora:~$ df -h
```

En el comando de arriba -h no quiere decir help, sino "leible por humano" 
(human-readable). En vez de escribir un numero entero gigante de bytes.
Algunos comandos usan esta convencion para mostrar tamaños de discos y
archivos, con K para mostrar en kilobytes, G para Gigabytes y asi.

`du` muestra el espacio usado por una carpeta y sus subcarpetas. Si usted desea
saber cuanto espacio tiene libre el disco actual, use el comando `df`.

```bash
usuario@computadora:~$ du -h
4.0K    ./.landscape
4.0K    ./.nedit
4.0K    ./.config/procps
8.0K    ./.config/htop
16K     ./.config
4.0K    ./notasAgus/.git/branches
56K     ./notasAgus/.git/hooks
12K     ./notasAgus/.git/objects/be
8.0K    ./notasAgus/.git/objects/98
4.0K    ./notasAgus/.git/objects/pack
8.0K    ./notasAgus/.git/objects/14
8.0K    ./notasAgus/.git/objects/89
8.0K    ./notasAgus/.git/objects/0b
8.0K    ./notasAgus/.git/objects/9e
8.0K    ./notasAgus/.git/objects/b5
4.0K    ./notasAgus/.git/objects/info
8.0K    ./notasAgus/.git/objects/1a
8.0K    ./notasAgus/.git/objects/65
8.0K    ./notasAgus/.git/objects/ca
96K     ./notasAgus/.git/objects
8.0K    ./notasAgus/.git/info
4.0K    ./notasAgus/.git/refs/tags
8.0K    ./notasAgus/.git/refs/heads
16K     ./notasAgus/.git/refs
8.0K    ./notasAgus/.git/logs/refs/heads
12K     ./notasAgus/.git/logs/refs
20K     ./notasAgus/.git/logs
224K    ./notasAgus/.git
248K    ./notasAgus
4.0K    ./.local/share/nano
8.0K    ./.local/share
12K     ./.local
320K    .
```

Con `du` utilice la bandera `--max-depth='N'` para que solo vea N niveles de 
subcarpetas, desde la carpeta especificada.

```bash
usuario@computadora:~$ du -h --max-depth=1
4.0K    ./.landscape
4.0K    ./.nedit
16K     ./.config
248K    ./notasAgus
12K     ./.local
320K    .
```

`ps` muestra todos los usuarios corriendo actualmente ejecuatando procesos

```bash
usuario@computadora:~$ ps
PID   TTY          TIME CMD
   10 pts/0    00:00:00 bash
   74 pts/0    00:00:00 nano
   78 pts/0    00:00:00 ps
```

### Miscelaneos

#### `paswd / logout / exit`

Cambiar la contraseña de la sesion con `passwd`. Preguntara por la contraseña 
actual para verificacion, y luego ingrese dos veces la contraseña nueva, asi 
que no se equivoque al escribir.

```bash
usuario@computadora:~$ passwd
Changing password for usuario.
(current) Linux password:	(escriba la contraseña actual)
Enter new Linux password:	(escriba la nueva contraseña)
Retype new Linux password: 	(escriba de nuevo la nueva contraseña)
passwd: password updated successfully
```

`logout` termina la session de la terminal actual.

```bash
usuario@computadora:~$ logout
Session stoped
```

> - Presione retroceso para salir de la ventana
> - Presione R para reiniciar la sesion
> - Presione S para guardar el archivo de salida de la terminal

`exit` permite salir de cualquier terminal

```bash
usuario@computadora:~$ exit
Session stopped
```

#### `celar / *`

Ejecute `clear` para mover la linea actual de la termina a la parte de arriba de
la ventana. Este comando borra las lineas de arriba de la ejecucion de la terminal.
Es bueno para limpiar su espacio de trabajo.

Utilice el asterisco * cuando este buscadno archivos. Muestra las coincidencias 
de los caracteres de la direccion que escribimos.

```bash
usuario@computadora:~$ ls Git/Parser/source/PD*
Git/Parser/source/PDateTimeUtils.java   Git/Parser/source/PDelimitedFile.java
```

El asterisco puede ser usado muchas veces en un comando y que coincida con cero
o mas caracteres.

```bash
usuario@computadora:~$ ls Git/Parser/source/P*D*m*
Git/Parser/source/PDateTimeUtils.java   Git/Parser/source/PDelimitedFile.java
```

## Intermedio

### Uso de disco, memoria y cpu

#### `ncdu`

#### `top / htop`

`top` muestra un lista de los procesos ejecutandose actualmente, sus propietarios,
uso de memoria y mas. `htop` es una version mejorada. (Nota: podes usar la bandera
`-u username` para restringir la lista de procesos a aquellos que solo pertenecen
a `username`.

### REPLs y versiones de software

#### REPLs

Un RELPs es una ejecucion de un interprete interactivo (Read-Evaluate-Print Loop),
es similar a la linea de comandos de la terminal, pero ejecuta el motor de otro 
lenguaje, ya sea Python con `python3`, Java con `jshell`, R (el lenguaje) con `R`,
y mas lenguajes.

Para salir de python usar `quit()`
Para salir de java usar `/exit`
Para salir de R usar `q()`

Tambien para salir de cualquiera de las REPLs se puede usar ^d (ctrl + d), que es
el fin del archivo (EOF end of file), este es un atajo de linux para terminar
la entradas.

#### `-version / --version / -v`

La mayoria de los comandos y programas tienen una bandera -version o --version,
que devulve la version del comando o programa. La mayoria de las aplicaciones
muestra esta informacion facilmente.

```bash
usuario@computadora:~$ ls --version
ls (GNU coreutils) 8.30
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Written by Richard M. Stallman and David MacKenzie.

usuario@computadora:~$ du --version
du (GNU coreutils) 8.30
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjorn Granlund, David MacKenzie, Paul Eggert,
and Jim Meyering.

usuario@computadora:~$ python3 --version
Python 3.8.10
```

Pero algunos puede ser menos intuitiva la forma de obtener esta informacion.

```bash
usuario@computadora:~$ sbt scalaVersion
(info) 2.12.4
```

Tenga en cuenta que algunos programas usan `-v` como la bandera de version, y otros
programas usan `-v` con el significado de 'vervose', que ejecutara la aplicacion
imprimiendo en consola informacion para diagnostico y debugging.

![Manual de scp](/img/cap_ej_version1.jpg)

### Alias y variables de ambiente

#### Variables de ambiente

**Variables de ambiente** (algunas veces acortado como "env vars") son variables 
persistentes, que pueden ser creadas y utilizadas por la terminal `bash`. Son 
definidas con el signo `=` y evocadas con el signo `$`. Usted puede ver todas
las variables de ambientes definidas actualmente con el comando `printenv`.

```bash
usuario@computadora:~$ printenv
SHELL=/bin/bash
WSL_DISTRO_NAME=Ubuntu-20.04
NAME=laptop-agus
PWD=/home/agus_ra
LOGNAME=agus_ra
MOTD_SHOWN=update-motd
HOME=/home/agus_ra
LANG=C.UTF-8	
```

Para setear una nueva variable de ambiente con un signo `=` (no pongas especios
antes ni despues del `=`)

```bash
usuario@computadora:~$ myvar=hello
```

Para inprimir una variable con `echo` y poniendo el signo `$` antes del nombre 
la variable.

Las variables que contengan espacios o otros tipos de espacio en blanco, deberan
rodearse con comillas. Tenga en cuenta que al reasignar un valor a una variable
de ambiente se sobre escribira sin advertencia.

```bash
usuario@computadora:~$ myvar="hello, world!" && echo $myvar
hello, world!
```

Las variables tambien se pueden definir con el comando `export`. Cuando son
definidas de esta manera tambien estan disponibles para los subprocesos convocados
en esta terminal.

```bash
usuario@computadora:~$ export myvar="another one" && echo $myvar
another one
```

Se puede *des-setear* la variable dejando un espacio en blanco despues de el 
signo `=` o al usar el comando `unset`.

```bash
usuario@computadora:~$ unset myvar

usuario@computadora:~$ echo $myvar
```
	
#### Alias

Los **alias** son similares a las variables de ambiente pero son usados de forma
diferente, se utilizan para remplazar comandos largos por comandos cortos.

```bash
usuario@computadora:~$ cd /mnt/c/Users/usuario/Desktop
usuario@computadora:/mnt/c/Users/usuario/Desktop$ pwd
/mnt/c/Users/usuario/Desktop

usuario@computadora:~$ alias ewin="cd /mnt/c/Users/usuario/Desktop"
usuario@computadora:~$ ewin && pwd
/mnt/c/Users/usuario/Desktop
usuario@computadora:/mnt/c/Users/usuario/Desktop$ _
```

Se pueden eliminar un alias con el comando `unalias`.

```bash
usuario@computadora:~$ unalias ewin

usuario@computadora:~$ ewin
Command 'ewin' not found, did you mean:
...
```

### Programacion basica en `bash`

#### Progrmas en `bash`

Los progrmas en  lenguaje `bash` usualmente terminados con la extencion `.sh`,
permiten automatizar procesos complicados de comandos en la terminal, 
empaquetarlos en funciones reutilizables. Un programa escrito en `bash` puede
contener cualquier numero de comandos normales de `shell`.

```bash
usuario@computadora:~$ echo "ls && touch file && ls" > ex.sh
```

Un programa de shell puede ser ejecutado con el comando `source` o el comando `sh`.

```bash
usuario@computadora:~$ source ex.sh
ex.sh		notasAgus
ex.sh		file		notasAgus
```

Los programas de shell pueden ser convertidos en ejecutables con el 
comando `chmod`.

```bash
usuario@computadora:~$ echo "ls && touch file2 && ls" > ex2.sh
usuario@computadora:~$ chmod +x ex2.sh
```

Un programa ejecutable de `shell` puede ser ejecutado con precediendolo con `./`.

```bash
usuario@computadora:~$ ./ex2.sh
ex.sh		ex2.sh		file		notasAgus
ex.sh		ex2.sh		file		file2		notasAgus
```

Las lineas largas de codigo pueden ser partidas poniendo al final una `\`

```bash
usuario@computadora:~$ echo "for i in {1..3}; do echo \
> \"Welcome \$i times\"; done" > ex3.sh
```

Los programas de `bash` puede contener ciclos, funciones y más.

```bash
usuario@computadora:~$ source ex3.sh
Welcome 1 times
welcome 2 times
Welcome 3 times
```

#### Personalizacion del resumen de `ls`

Los programas de `bash` pueden hacer tu vida mucho mas facil y mas colorida.
(conseguir el link a "bash scripting cheat sheet")

`$PS1` (Prompt String 1) es la variable de ambiente que define tu terminal 
principal.

```bash
usuario@computadora:~$ printf "%q" $PS1
```

( no estaria entendiendo mucho sobre este tema, asi que lo voy a dejar para 
despues)

### Archivos de configuracion

#### Archivos de configuracion / `.bashrc`

Si probas los comandos de la seccion anterior, y cerras sesion y volves a entrar,
vas a notar que tus cambios desaparecieron. Los archivos `config` te permiten 
guardar cambios persistentes para la terminal o un programa en particular, que 
estaran disponibles siempre que incies sesion o ejecutes el programa. El archivo
de configuracion principal de la terminal `bash` es `~/.bashrc`. Los alias, las
variables de ambiente, y las funciones añadidas a la `~/.bashrc` estaran 
disponibles en todo momento en la sesion configurada. Los comandos en el 
archivo `~/.bashrc` se ejecutaran cada vez que inicies sesion.

Si editas tu archivo `~/.bashrc`, podes re-cargarlo sin necesidad de cerrar sesion
y volver a iniciar sesion nuevamente, usando el comando `source`.

```bash
usuario@computadora:~$ nano ~/.bashrc
```

Agrega la linea `echo "~/.bashrc loaded!"` en la parte de arriba del archivo, esta
linea nos servira para ver cuando se a cargado el archivo de configuracion de 
la terminal.

```bash
usuario@computadora:~$ source ~/.bashrc
~/.bashrc loaded!
```
Al iniciar sesion tambien aparecera el mensaje de cargado.

```bash
~/.bashrc loaded!

usuario@computadora:~$
```

#### Tipos de terminales (shells)

*Login shells* son terminales en las que podes iniciar sesion (donde tenes nombre
de usuario). *Interactive shells* son la terminales que aceptan comandos. Las 
terminales pueden ser *login* y *interactive*, *non-login* y *non-interactive*, y 
cualquier otra combinacion.

Aparte de `~/.bashrc`, hay otros archivos que alimentan automaticamente la terminal
cuando se inicia sesion y cuando se cierra sesion. Estos son:

> - `/etc/profile`
> - `~/.bash_profile`
> - `~/.bash_login`
> - `~/.profile`
> - `~/.bash_logout`
> - `/etc/bash.bash_logout`

