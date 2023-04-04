# Arquitectura y sistemas operativos
Clase del 17/08/22

## Temas de la clase

## Funcionalidades de un sistema operativo

- Para comprender la arquitectura de una computadora es necesario entender como funciona un Sistema Operativo.
- Las funcionalidades básicas de un sistema operativo son:

1. Actuar de interfaz entre el usuario y el hardware de manera transparente para el usuario. Ofreciendo un soporte a los usuarios para que sus acciones se transmitan con facilidad. No es necesario que sean especialistas en software o hardware para usarlo.
2. Gestionar los recursos de software y hardware del equipo. El uso eficiente de los recursos es primordial puesto que son limitados. Dependiendo del fin y las tareas encomendadas al sistema informático, la eficiencia puede redirigirse a acciones diferentes.

El sistema operativo es un software con características particulares, ya que debe administrar todos los recursos del sistema entre los usuarios y el resto de software.

Por lo tanto, las características fundamentales que debe soportar cualquier sistema operativo son:

> *Adaptabilidad*: Se debe acomodar a dos situaciones que evoluacionan en paralelo, nuevo software y nuevo hardware. EL sistema operativo debe ser capaz de reacondicionarse (normalmente mediante actualizaciones) para hacer uso de nuevas características o mejoras, tanto en componentes físicos como software.

> *Facilidad de uso:* teniendo como referente el fin al que se empleará el sistema informático, la facilidad de manejo ha de ser primordial. Normalmente, una mayor comodidad implica mayor gasto de recursos (como por ejemplo un sistema gráfico de ventanas). Por ello, existen sistemas operativos que ganan en eficiencia a costa de restringir su manejabilidad.

> *Eficiencia:* los recursos (procesadores y núcleos, RAM, acceso a discos, red o cola de impresión) son limitados. El sistema operativo debe atender todas las peticiones de usuarios, programa y el propio sistema operativo para facilitar el acceso a los recursos. Ello debe hacerse barajando la importancia de cada solicitud y quién desee hacer uso de los recursos. Esta tarea es muy compleja y crítica, ya que repercutirá en todo el sistema.

El sistema operativo debe administrar de forma eficiente los recursos, atendiendo al objetivo de dicho sistema operativo. Los más solicitados son:

> Memoria RAM: La parte del sistema operativo que siempre reside en memoria RAM se denomina núcleo o kernel. Es un subconjunto software del propio sistema operativo que por su importancia en la gestión del sistema no puede abandonar la memoria principal. El resto de los módulos del sistema operativo se irá cargando y descargando desde los dispositivos de almacenamiento secundario a la memoria principal, dependiendo de la arquitectura del sistema operativo. El espacio restante de la memoria RAM se debe gestionar eficientemente para albergar el resto de software y los datos que maneje este.

> Procesador: Aunque disponga de varios núcleos y, por tanto, pueda ejecutar varios procesos a la vez, existe multitud de software que desea ejecutarse.

> Adaptadores de red. Múltiples aplicaciones hacen uso de la red simultáneamente, debiendo administrar las conexiones de red entre aplicaciones, procesos y usuarios.

> Medios de almacenamiento: El acceso a discos duros puede representar un cuello de botella importante. 

> Colas de impresión: Pueden existir más de una petición de impresión a una misma impresora, por lo que se debe gestionar la cola de trabajos de impresión adecuadamente

## Tipos de sistemas operativos

Existen distintos puntos de vista para catalogar los sistemas operativos:

Atendiendo al número de procesos que se pueden ejecutar concurrentemente:

- Monotarea o monoprogramado: Un proceso únicamente puede ser ejecutado por un usuario. Esto quiere decir que un usuario solo puede estar ejecutando un programa, además del propio sistema operativo. 
- Multitarea o multiprogramado: un usuario puede ejecutar varios procesos simultáneamente. De esta manera, pueden existir varios programas en memoria susceptibles de ser ejecutados.

Atendiendo al número de usuarios que pueden ser atendidos por el sistema operativo simultáneamente:

- Monousuario: solo pueden atender a un usuario. El usuario goza de todos los recursos, a menos que el sistema operativo los acapare.

- Multiusuario: Pueden atender a más de un usuario concurrentemente. Por lo tanto, los recursos del sistema deben ser gestionados para todos ellos.

Atendiendo al tipo de procesamiento: el sistema operativo ha de estar preparado para ejecutar procesos con diferentes finalidades y requisitos. Los sistemas operativos intentan optimizar sus recursos, independientemente de los procesos que atiendan. Sin embargo, los procesos, según su forma de ejecutarse, pueden ser:

- De tiempo real: requieren unos plazos en su ejecución o tiempos de respuesta
- Interactivos: requieren de la participación del usuario.
- Por lotes, batch o no interactivos: se suministra un conjunto de tareas al sistema operativo con características similares, y este se encarga de ejecutarlas en serie y sin la intervención del usuario. En caso de producirse un error en una tarea del lote, el resto de tareas no se podrá ejecutar. Ejemplos: realización de facturas agrupadas, tareas de cómputo en investigación, envío de mensajes con informes o resúmenes en cadenas de producción, etc.

> Tener en cuenta: Los sistemas operativos multiusuario son multitarea, puesto que tratan con diferentes procesos asociados a varios usuarios. Por lo tanto, un sistema operativo multiusuario y monotarea, puede tratar con varios usuarios simultáneamente, pero con un único proceso por usuario. Es de reseñar que pueden existir sitemas multiusuario y monotarea, así como multitarea y monousuario.

De esta manera, existen sistemas operativos más orientados a uno u otro tipo de proceso, puesto que la eficiencia de estos se planifica desde el diseño de los mismos:

- Sistemas operativos en tiempo real: Donde se deben cumplir escrupulosamente los plazos de ejecución de los procesos y, además, deben tener un comportamiento predecible. Ejemplos: en aviónica, instrumentación médica, sistemas de alertas en una central nuclear, etc.

- Sistemas operativos interactivos o de tiempo compartido: orintados a la participación continua del usuario, los cuales hacen uso de los programas antes comentados, tales como un procesador de textos o un editor de imágenes. Son sistemas de propósito general en lo que, a diferencia de los sistemas de tiempo real, no priman los tiempos de respuesta en la ejecución de procesos. En esta clasificación de encuentran los más conocidos por nosotros como las diferentes versiones de escritorio y de red de Microsoft Windows o de Apple (Mac OS), así como distribuciones Linux, como Ubuntu

### Atendiendo al sistema de interfaz empleado:

- Textuales: Emplean un repertorio de comandos que de introducen en el sistema de forma escrita a través de un terminal de órdenes. Aunque, se necesitan mayores conocimientos de sintaxis y manejo del sistema operativo, las acciones pueden llegar a ser muy potentes desde un punto de vista de explotación del sistema operativo.
- Gráficos: Usan un conjunto de ventanas, botones y desplegables gráficos donde se representan los diferentes volúmenes, unidades y sistemas de ficheros de forma muy intuitiva. Además, los programas lanzados presentan una vista gráfica. El manejo se realiza con un dispositivo de entrada/salida, como el ratón, y destaca por su fácil utilización. Este sistema emplea muchos más recursos que el textual a nivel de procesador, memoria e incluso, en algunos casos, se necesita de manera casi obligada un adaptador gráfico. Por lo tanto, en sistemas operativos donde se busca ahorrar todo tipo de recursos en favor de atender a peticiones de usuarios y procesos, la interfaz gráfica se desprecia.

### Atendiendo a la forma de ofrecer los servicios

- Sistemas operativos cliente o de escritorio: Se encargan de realizar el procesamiento de la información, la gestión de los procesos, de la memoria, dispositivos de E/S de una sola computadora. Esta computadora suele estar conectada en red, pero el usuario es consciente de sus accesos externos. En un entorno corporativo, se pueden emplear prácticamente para compartir archivos en red. Por tanto, este tipo de sistema operativo  es el normalmente empleado en un hogar o pequeña oficina, así como en entornos empresariales en el ámbito de un servicio de directorio en una red distribuida. 
- Sistemas operativos en red: Se encargan de gestionar la red, los usuarios y los recursos de una red de computadoras en general, de forma centralizada mediante un servidor o varios como réplicas o extensiones del primero. Es en el servidor donde se instala este sistema operativo. El resto de equipos de la red (con sistemas operativos cliente) se conectan al servidor (de forma consciente) formando parte del sistema e interactuando con él. Su principal objetivos es el intercambio de información centralizada. Sin embargo, el servidor puede resultar un cuello de botella si cae o si se deteriora la transferencia de información. Destacan por su seguridad y robustez en la administración general del sistema y la gestión de la información que gestionan frente a los sistemas operativos de escritorio.
- Sistemas operativos distribuidos: A diferencia de los anteriores, actúan varios computadores de manera transparente al usuario, de forma que da la sensación que este interactúa solo con uno de ellos. Por tanto, permiten emplear los recursos de varias computadoras en paralelo.

## Actividades:

1. Realizar un mapa mental con MindMeinster (actividad grupal) desarrollar los puntos principales sobre Sistemas Operativos. Entregar uno solo por grupo con nombre de integrantes.

2. Responder las siguientes preguntas sobre lo visto  de sistemas operativos: (Actividad grupal) Nombre del grupo y los integrantes que participaron. Enviar al correo de la profesora 1 sólo trabajo por grupo.

    - ¿Cuáles son las funcionalidades básicas de un sistema Operativo? Desarrollar
    - ¿Cuáles son la características fundamentales de un SO?
    - Buscar ejemplos 2 o 3 de cada uno de los sistemas multiusuario y monotarea, y de multitarea y monousuario.
    - Buscar en internet dos versiones de sistema operativos únicamente textuales y explica por qué no presentan interfaz gráfica. Buscar dos versiones gráficas de sistemas operativos.
