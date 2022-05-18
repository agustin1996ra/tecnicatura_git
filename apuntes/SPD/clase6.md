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
cambios, los debemos hacer a travez de las ramas auxiliares.

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

Vamos a crear un documento para que luego sea ignorado por git
de nombre requisitos




### Para movernos de una rama a otra

```
git checkout master

git switch nombre_de_rama
```
### Para ver las ramas que tengo

```
git branch
```

### Como configurar de manera global el nuevo nombre de la rama master

