# Clase 6: comandos y funcionalidades

> # Repaso clase anterior
>
> - `git checkout -b`
> - `git branch`
> - `git switch`
> - `git merge`

## Funcionalidades de nuestras ramas

Una rama es un espacio temporal donde vamos a trabajar diferentes funcionalidades que van a ser agregadas a nuestro proyecto.

La rama main va ser la rama principal de todos el proyecto.

Git nos va a permitir ir avanzando de manera cronológica
sobre nuestro proyecto.

También podremos viajar en el tiempo y volver a consultar 
modificaciones anteriores.

## Nuestra rama main es un espacio temporal

Aquí es donde nosotros trabajamos con nuestro proyecto.

Cada punto representa una confirmación, osea un avance, una
nueva funcionalidad, un punto en el tiempo.

A medida que nuestro proyecto avanza vamos trabajando en 
modificaciones o actualizaciones que vamos haciendo para su 
mejora.

Estas modificaciones las va a realizar de manera cronológica, 
de manera lineal, tenemos nuestra rama donde vamos trabajando,
nuestro proyecto, nuestro repositorio.

## No siempre los cambios que realicemos serán utilizados en nuestro proyecto

Hay ocasiones en las que un cambio no necesariamente va a 
ser aplicado al proyecto.

Puede ser un cambio que el cliente ha pedido y que nada más es
para prueba.

Puede ser un cambio que el proyecto no amerita al final de todo.

Por éste motivo hacemos uso de las ramas auxiliares.

Una regla general de git es que en la rama main nunca se
debe trabajar en los cambios, solo en ramas auxiliares.

Hay una regla que dice que en la rama main nunca se debe trabajar
cambios, los debemos hacer a traves de las ramas auxiliares.

Ahora bien, si en dado caso nosotros queremos que estos
cambios si se incorporen a la rama main, osea al proyecto como 
tal.

Cuando hacemos cambios en el proyecto, que no estamos seguros
que se van a implementar, simplemente podemos elimiarlos, pero
no va a haber ningún cambio sobre la rama main. Y a eso es a lo
que se le conoce como trabajo con ramas.

## Funcionalidad del merge

Cuando hacemos un `merge`, estamos realizando la unión de una
rama temporal a la main.

En el último punto se realiza la unión y los puntos del 
commit que hicimos en nuestra rama auxiliar se unen con los commit de nuestra **rama main**.

## ¿Como se trabaja con Git?

> Por lo general siempre se trabaja con ramas.
>
> Siempre tendremos una rama principal (`master` o `main`) y 
>ramas auxiliares.
>
> La rama main no podemos tocarla.

## ¿Quiénes son los únicos que van a poder trabajar sobre la master?

Siempre en cada proyecto habrá líderes, ellos serán los únicos
que estarán a cargo de modificar la main, los demás integrantes
no estarán autorizados.

## Creación de ramas

Desde las ramas de cada desarrollador, se sacarán ramas para
trabajar en la rama que le queda a cada uno.

Una vez que se cumple el trabajo en cada rama se debe volver a 
la rama main.

## Cuando ejecutamos el `merge`

Cuando hablamos de utilizar el comando `merge`, hablamos de la
integración de las ramas auxiliares (que se han estado trabajando
por separado) a nuestra rama main.

Puede que en la creación de esas ramas auxiliares hemos estado 
tocando los mismo archivos en diferentes ramas, esto puede
generar conflictos.

## Cambio sólo realizados en nuestras ramas auxiliares:

Todos los cambios que realizaremos en nuestro proyecto los
realizaremos en nuestras ramas **auxiliares** para luego pasarlos
a nuestra rama **main**.

Una vez que ya confirmamos nuestros cambios en nuestras ramas
**auxiliares**, son enviados a la **main**.

Allí los líderes controlarán que los cambios realizados 
funcionen.

# Comandos

## Nuestra carpeta `.gitignore`

Es un carpeta creada en el directorio de trabajo en el momento 
se ejecutar `git init`. Esta carpeta contiene reglas sobre qué 
archivos y/o carpetas deben ser ignorados por git.

Cualquier archivo que ignoremos no aparecerá en la salida de un 
`git status` y ademas será ignorado cuando utilicemos un comando
`git add .`. Esto no quiere decir que los archivos ignorados
sean eliminados de tu equipo local, si no que permanecerán ahí 
pero nunca se subirán al repositorio.

## Ingnorando archivos

Para ignorar archivos utilizaremos el comando:

```
$ git ignore
```

Este comando nos permite mover los archivos que no utilicemos en nuestras
ramas de git.

## Para cambiar de una rama a la otra

En las clases anteriores estuvimos utilizando los comandos
```
$ git checkout master

$ git switch nombre_de_rama
```

## Para ver las ramas que tengo

Uno de los comandos que utilizamos para visualizar las ramas creadas

```
$ git branch
```


## Como configurar de manera global el nuevo nombre de la rama master

Podemos cambiar el nombre de nuestra rama master a través de una configuración
global.

```
$ git branch
```
Este comando nos permite visualizar las ramas que tengo

### Para cambiar el nombre de las ramas:

Para camiar el nombre de la rama master a main

```
$ git branch -m master main
```

Este comando solo te permite cambiar el nombre de la rama master a main o 
al revés de main a master.

### Como configurar de manera global el nuevo nombre de la rama master?

Para modificar el nombre de la rama master cada vez que el repositorio se inicia
y se inicie con el nuevo nombre se debe hacer una configuración global.

Usando:

```
$ git config --global init.defaultbranch master main
```

Luego usamos el comando:

```
$ git config --list
```
Para ver los cambios.

## Proyectos en git

Cuando trabajamos proyectos en git por lo gneral trabajamos con diferentes
versiones de nuestro proyecto. Los desarrolladores prefieren llevar siempre un
proyecto por versiones, por paso o por diferentes puntos:

- Se revisa el producto
- Se realiza un testing rápido y se verifica que el proyecto vaya conforme a lo
pedido.

## Los tags

**Git** nos permite crear este tipo de seguimiento o versiones.
Para ello nos da los **tags**, un tag o etiqueta también es un identificador
que nos permite seleccionar un grupo de modificaciones o cambios que realizamos
y agruparlas en una version o **tag**.

El comando que utilizaremos para ordenar nuestras diferentes versiones del 
proyecto en el que estemos trabajando es el siguiente.

```
git tag nombre_de_la_etiqueta
```

Es importante seleccionar sólo los commit que van a ser parte de esa version
y llevaran una etiqueta.

¿como realizar la selección de los commit que quiero versionar o separar con una
etiqueta?

Para ello usaremos el comando:

```
git rest --hard hash
```

Solo quedan seleccionados los commit hasta el numero de hash que seleccionamos,
esos commit serian los que formarán parte de la version o etiqueta.

Para comprobar si mi etiqueta usamos el siguiente comando

```
$ git tag
```

Nos mostrara la etiqueta sobre la que estamos trabajando o que tenemos 
hasta el momento. 

Usando el comando:

```
git show
```

Veremos la información de los cambios realizados en los archivos guardados en
commit actual de la version mas reciente

Para ver com se dispone la información en el gráfico de ramas usamos el
comando:

```
git log --oneline --all --graph --decorate
```

Observaremos como se muestra las etiquetas en los commits.

### Tags con comentarios

Seleccionamos uno de los commit desde donde queremos que figure
nuestra etiqueta de nuestra version.

Para ello utilizaremos:

```
git tag -a nombre -m "comentario" hash_de_commit
```

Por ejemplo:

```
git tag -a v1.0 -m "primera version de mi proyecto" 7bc3d84
```

## Cuando nos encontramos modificando archivos y se nos solicita unas nuevas modificaciones

Cuando nos encontramos modificando, trabajando o creando más archivos
de nuestro proyecto, ya sea porque vamos avanzando o porque simplemente
hay modificaciones que hacer, es muy probable que en algún punto 
tengamos que hacer algo asi como un freno de emergencia, como un 
stop de emergencia.

Por ejemplo: Si estamos trabajando en algún archivo y de pronto el 
cliente pide una actualización urgente o un cambio que es de vida o
muerte, es algo que debe hacerse en el momento.

Pero aún no se ha terminado con las modificaciones que se estaban 
realizando, no has acabado con tu progreso por multiples razones.

cómo vamos a solucionar esto?

### `git stash`

Me permite generar un campo temporal en el que se va a guardar el progreso de nuestro proyecto.

Hacemos la modificación que el cliente pide y ya luego podemos continuar en donde lo habíamos dejado.

Vamos a teclear `git stash`.

Y nos guardará los cambios sin que se alteren las modificaciones en 
que estamos trabajando.

Para realizar las modificaciones que nuestro cliente nos esta pidiendo
con urgencia.

Luego ejecutaremos `git add` y commitearemos las modificaciones.

```
git commit -am "mensaje del commit"
```

Luego con el comando 

```
git stash pop
```

Recuperaremos las modificaciones en las que estábamos trabajando y
podremos seguir trabajando en ellas.

El comando `git stash` me permite guardar las modificaciones que
estaba realizando para atender alguna modificación más urgente y 
después seguir trabajando en lo que estaba realizando.

Añado las modificaciones de urgencia y luego ejecuto el 
comando `git stash pop` y me aparecerán las modificaciones
en las que estaba trabajando y que ya están listas para 
añadir y commitear.