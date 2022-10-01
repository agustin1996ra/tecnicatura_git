# Trabajo práctico grupal
## Grupo: MATE CODERS

### Integrantes:

- Facundo Martin Giacomozzi
- Gabriel Romero
- Lautaro Urquiza
- Federico Pfund
- Matias Canevaro
- Eduardo Luis Gómez
- Sabrina Mantero
- Cinthia Fernanda Segovia
- Martín Alejandro Torres
- Agustin Rodriguez Alvarez

## Consignas
En grupo responder las siguientes preguntas:
1. Requerimientos de hardware que LINUX necesita.
2. Funcionamiento del Kernel de LINUX.
3. Realizar una linea de tiempo de LINUX con el año y las actualizaciones que se fueron realizando.

# Respuestas

## 1. Requerimientos de hardware que LINUX necesita

Los requisitos mínimos de hardware para una version mínima del SO:
- Procesador: intel 80386
- Memoria RAM: 4Mb, recomendable 8Mb
- Disco duro: 20Mb de espacio libre, recomendable 100Mb
- Unidad de CD-ROM

Para versiones de escritorio de distribuciones de LINUX populares:

### Debian


#### Version normal
Requisitos mínimos para sistemas con interfaz gráfica:
- Procesador: Pentium 4 a 1GHz
- Memoria RAM: 1Gb
- Disco Duro: 10Gb

Requisitos recomendados para sistemas con interfaz gráfica:
- Procesador: Pentium 4 a 1Ghz
- Memoria RAM: 2Gb
- Disco Duro: 10gb

Requisitos mínimos para sistemas sin interfaz gráfica:
- Procesador: Pentium 4 a 1GHz
- Memoria RAM: 256Mb
- Disco Duro: 2Gb

Requisitos mínimos para sistemas sin interfaz gráfica:
- Procesador: Pentium 4 a 1GHz
- Memoria RAM: 256Mb
- Disco Duro: 2Gb

#### Versiones reducidas
Estas versiones pueden ser instaladas con un mínimo de 20Mb de RAM en arquitecturas de procesador s390 y 60Mb en arquitecturas de amd64. A la hora de calcular el espacio necesario para el disco duro, tenemos que ir teniendo en cuenta que partes del sistema vamos a utilizar y las aplicaciones que necesitamos instalar.

### Ubuntu 22.04 version de escritorio

Requisitos mínimos de hardware:
- Procesador: 2GHz dual core
- Memoria RAM: 4Gb
- Disco Duro: 25Gb (Puede ser un LiveCD)
- Salida de video: Puerto VGA 1024x768 resolución
- Un puerto USB o una Lectora de CD/DVD

Datos obtenidos de: []
### Fedora 36

Requisitos recomendados de hardware:
- Procesador: 2GHz quad core
- Memoria RAM: 4Gb
- Disco Duro: 20Gb

Requisitos mínimos de hardware:
- Procesador: 2GHz dual core
- Memoria RAM: 2Gb
- Disco Duro: 15Gb

Datos obtenidos de: [Fedora Project - Hardware Overview](https://docs.fedoraproject.org/en-US/fedora/latest/release-notes/welcome/Hardware_Overview/)

## 2. Funcionamiento del Kernel LINUX

El kernel de Linux es el elemento principal de los sistemas operativos Linux, y es la interfaz o conexión fundamental entre el hardware de una computadora y sus procesos. Los comunica entre sí y gestiona los recursos de la manera más eficiente posible.

### El kernel cumple cuatro funciones:
1. Gestión de la memoria: supervisa cuánta memoria se utiliza para almacenar qué tipo de elementos, así como el lugar en que los guarda.

2. Gestión de los procesos: determina qué procesos pueden usar la unidad central de procesamiento (CPU), cuándo y durante cuánto tiempo.

3. Controladores de dispositivos: actúa como mediador o intérprete entre el hardware y los procesos.

4. Seguridad y llamadas al sistema: recibe solicitudes de servicio por parte de los procesos.


### Arquitectura simplificada y ubicación del kernel

Para darle un contexto al kernel, imagínese que el equipo Linux tiene tres capas:

1. El hardware: Se trata del equipo físico, el cimiento o la base del sistema, que esá compuesto de la memoria (RAM) y el procesador o la unidad central de procesamiento (CPU), además de los dispositivos de entrada y salida (E/S), el almacenamiento, la conexión de red y los gráficos. La CPU realiza los cálculos y también accede a la memoria y la modifica.

2. El kernel de Linux: el corazón del SO. Se encuentra justo en el medio y se trata del software que reside en la memoria e indica qué debe hacer la CPU.

3. Procesos del usuario: son los programas en funcionamiento que gestiona el kernel y, en conjunto, conforman el espacio del usuario. También se les llama procesos simplemente. El kernel también permite que los procesos y los servidores se comuniquen entre sí, lo cual se conoce como comunicación entre procesos (IPC).



Información obtenida de: [RedHat - ¿Qué es el kernel de Linux?](https://www.redhat.com/es/topics/linux/what-is-the-linux-kernel)
