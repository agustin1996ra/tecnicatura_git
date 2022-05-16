# Clase 6 de Programacion 

Clase del dia 13/05/2022
Avanzamos en Java.

## Actividades de la clase

- Cuestionario sincronico de los temas de clase
- Ejercicios habilitados al terminar la clase a resolver con el grupo
a entregar el lunes por mail a Ariel.

## Tipos primitivos en Java (parte3)

### Tipo de variable booleana

```java
boolean varBool = true;
System.out.println("varBool = " + varBool);
```

#### `if / else`

Es importante prestar atencion a las llaves `{ }` ya que si eliminamos
algunas de las llaves correspondientes al bloque de codigo del
condicional puede generarnos errores.

```java
if (varBool) {
    System.out.println("La bandera es verde");
}
else{
    System.out.println("La vandera es roja");
}
```
### Ejercicio: Algoritmo ¿eres mayor de edad?

```java
var edad = 30;
// var adulto = edad >= 18; // Esta es una expresión booleana
if (edad >= 18){
    System.out.println("Eres mayor de edad");
}
else{
    System.out.println("No eres mayor de edad");
}

```

### Conversion de tipos primitivos

En este caso debemos notar que no es lo mismo procesar con 
`Integer.parseInt()` que no hacerlo. Vemos los ejemplos con la 
concatenacion de variables y la suma de enteros dentro `sout`.

```java
var edad = Integer.parseInt("20"); // La clase integer con el metodo parseint, transforma la cadena en un entero
System.out.println("edad = " + (edad + 1)); // resultado sera 21
        
var edad1 = "20"; // tipo cadena
System.out.println("edad1 = " + (edad1 + 1)); // esto nos dara como resultado 201
```

La forma de transformar una cadena a double es utilizando 
`Double.parseDouble("3.1416")`

```java
var valorPI = Double.parseDouble("3.1416");
System.out.println("valorPI = " + valorPI);
```

A la hora de pedir un valor

```java
var entrada = new Scanner(System.in);
System.out.println("Digite su edad:");
edad = Integer.parseInt(entrada.nextLine());
System.out.println("entrada = " + entrada);
System.out.println("edad = " + edad);
```

### Tipo caracter y string

```java
var edadTexto = String.valueOf(10);
System.out.println("edadTexto = " + edadTexto);
        
var fraseChar = "programadores".charAt(12);
System.out.println("fraseChar = " + fraseChar);
        
System.out.println("Digite un caracter");
var entrada = new Scanner(System.in);
fraseChar = entrada.nextLine().charAt(0); // por mas que pongamos una cadena, solo tomara el carater en el indice especificado.
System.out.println("fraseChar = " + fraseChar);
```

