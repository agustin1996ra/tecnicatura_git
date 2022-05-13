# Fundamentos Java

## Inferencia de tipos `var`:

Este es un tipo de asignación de variable que infiere de que tipo de variable primitiva 
le estamos dando como valor.

```java
var num = 10; // La variable num sera de tipo int, por no tener punto.
var num1 = 10.5; // La variable num1 sera de tipo double por usar el punto.
var num2 = 10.5F; // Con la precencia de el punto y la letra 'F' al final iterpreta que es un float.
```


### Tipos primitivos:

> Después de los tipos enteros y flotantes, podemos entender mejor el uso de `var`

Vamos a practicar en NetBeans

## Ejecución paso a paso

Ejecución paso a paso o debugfile. Para utilizarlo es necesario agregar un punto de 
ruptura.

### Puntos de ruptura

Es una indicación para que la ejecución del programa se interrumpa. Se aplica haciendo
botón secundario en el indice de la línea de código que se desea. Los puntos
de ruptura solo se pueden en una línea de código valida.

## Variables tipo char

Los caracters permitidos son los caracteres de la lista unicode

[link]


### Practica de la clase:

````java
char varCaracter = '\u0024'; // Indicamos a Java la asignación con el código unicode
System.out.println("varCaracter = " + varCaracter);
char varCaracterDecimal = 36; // Valor decimal del juego de caracteres unicode
System.out.println("varCaracterDecimal = " + varCaracterDecimal);
char varCaracterSimbolo = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
```

Utilizando la inferencia con el tipo `var`

```java
var varCaracter1 = '\u0024'; // Indicamos a Java la asignación con el código unicode
System.out.println("varCaracter1 = " + varCaracter1);
var varCaracterDecimal1 = (char)36; // Valor entero y le asigna un tipo char
System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
var varCaracterSimbolo1 = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
```

Ejecutar este código para ver el funcionamiento de `char` y otra muestra de `var`.
