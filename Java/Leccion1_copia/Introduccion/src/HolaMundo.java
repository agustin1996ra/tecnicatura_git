
import java.util.Scanner;


public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("HolaMundo.main()");
        
        /*
        System.out.println("Hola mundo desde Java");
        
        // Tipo int - entero
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        // Tipo string
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        
        //Var - inferencia de tipos en Java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab
        //Para ejecutar Shift + F6
        
        var usuario = "Agustin";
        var titulo = "Tec. Electromecanico";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        
        // Ejercicio: Caracteres especiales con Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre); // Digonal inversa y letra n, para agregar una linea en el print
        System.out.println("Tabulador: \t" + nombre); //Tabulador son cuatro espacios 
        System.out.println("\t\t.:MENÚ:.");
        System.out.println("Retroceso: \b\b" + nombre); // Caracter de retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas dobles: \"" + nombre + "\"");
        */
        // Clase Scanner
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
        
        int entero;
        float decimal;
        String cadena; 
        String cadena2;
        
        
        System.out.print("Digite un numero entero:  ");
        entero = entrada.nextInt();
        System.out.println("El numero entero es  "+entero);
        System.out.print("Digite un numero flotante:  ");
        decimal = entrada.nextFloat();
        System.out.println("El numero decimal es  "+decimal);
        System.out.println("");
        System.out.print("Digite una cadena ");
        cadena = entrada.next();
        System.out.println("La cadena con next es "+cadena);
        System.out.println("");
        System.out.print("Digite una cadena con next line  ");
        cadena2 = entrada.nextLine();
        System.out.println("La cadena es "+cadena2);
        */
        
        // Tipos primitivos Enteros
        /*
        byte numEnteroByte = 127; // El valor minimo de byte -128 y el maximo 127
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;// Debemos agregar la letra "L" al final del número
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+ Long.MAX_VALUE);
        
        // Tipos primitivos Flotantes
        float numFloat = 3.4028235E38f; // Debemos agragar la letra "f" al final del número
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo de float: "+ Float.MIN_VALUE);
        System.out.println("Valor maximo de float: "+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157e308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo de double: "+ Double.MIN_VALUE);
        System.out.println("Valor maximo de double: "+ Double.MAX_VALUE);
        */
        // Inferencia de tipos var y tipos primitivos
        /*
        var numEntero = 20; // Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; // Automaticamente con el punto y la F se transforma en tipo float
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0; // Automaticamente con el punto se transforma en tipo double
        */
        
        // Tipos primitivos char
        /*
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
       
        
        char varCaracter = '\u0024'; // Indicamos a Java la asignación con el código unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; // Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; // Indicamos a Java la asignación con el código unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; // Valor entero y le asigna un tipo char
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        */
        
        // Tipos primitivos tipos booleanos
        /*
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if (varBool) {
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La vandera es roja");
        }
        */
        // Algoritmo: ¿Es mayor de edad?
        /*
        var edad = 30;
        // var adulto = edad >= 18; // Esta es una expresión booleana
        if (edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("No eres mayor de edad");
        }
        */
        // Conversion de tipos primitivos
        /*
        var edad = Integer.parseInt("20"); // La clase integer con el metodo parseint, transforma la cadena en un entero
        System.out.println("edad = " + (edad + 1)); // resultado sera 21
        
        var edad1 = "20"; // tipo cadena
        System.out.println("edad1 = " + (edad1 + 1)); // esto nos dara como resultado 201
        
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        */
        // Pedir un valor
        /*
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad:");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("entrada = " + entrada);
        System.out.println("edad = " + edad);
        */
        
        /*
        // Conversión de tipos primitivos (parte dos)
        
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter");
        var entrada = new Scanner(System.in);
        fraseChar = entrada.nextLine().charAt(0); // por mas que pongamos una cadena, solo tomara el carater en el indice especificado.
        System.out.println("fraseChar = " + fraseChar);
        */
        /*
        // Operadores
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma= " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion resta= " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion division= " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 = " + solucion2);
        */
        /*
        // Operadores Unarios: Cambio de signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); // El resultado será un nuemro negativo 
        
        // Operadores de negación
        var varC = true; //Esta literal por default en Java es de tipo boolean
        var varD = !varC; //Aquí se invierte el valor gracias al sino !
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores unarios de incremento: Preincremento
        var varE = 9; // Se va a modificar su valor 
        var varF = ++varE; // Note que el simbolo del incrememento est antes de la variable
        // Primero se incrtementa la variable "varE" y después se asigna su valor a "varF"
        // Por lo que las dos variables tendran el mismo valor.
        System.out.println("varE = " + varE);// se incrementa en una unidad
        System.out.println("varF = " + varF);// Se le asigna el valor de la otra varaiable incrementada
        
        // Postincremento (el simbolo va después de la variable)
        var varG = 3;
        var varH = varG++; // primero el valor de la variable y luego los sibolos del incremento
        System.out.println("varG " + varG);// Tenerb en cuenta que el valor de la "varG" se incremento
        System.out.println("varH = " + varH); // pero el valor asignado a la variable "varH" tiene
        //tiene asignado el valor antes del incremento, por que al leer de izquierda a derecha
        // lo primero que hace es asignar el valor, y despues incrementar la varG.
        
        //Operadores unarios de decremento: predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI); //La variable ya esta con decremento
        System.out.println("varJ = " + varJ); //Tendra el mismo valor que la variable "varI"
        
        // Postdecremento
        var varK = 8;
        var varL = varK--;// Priemro se asigna la variable y luego se la decrementa.
        System.out.println("varK = " + varK);// nos mostrara el decremento de "varK"
        System.out.println("varL = " + varL);
        */
        /*
        //Opeadores de Igualdad y Relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum); //operador de igualdad, resultado: true o false
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum; // Operador de diferentes, o no iguales.
        System.out.println("dNum = " + dNum);
        
        // en este caso veremos que no sirve para comaprar cadena usar directamente el operador ==
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        // Ya que solo comparara las referencias de la cadena y no su contenido
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        // para comaparar el contenido de los objetos de tipo string
        // usamos ".ecuals()"
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum > bNum;
        System.out.println("gVar = " + gVar);
        
        var hVar = aNum < bNum;
        System.out.println("hVar = " + hVar);
        
        var iVar = aNum >= bNum;
        System.out.println("iVar = " + iVar);
        
        var jVar = aNum <= bNum;
        System.out.println("jVar = " + jVar);
        
        var kVar = aNum != bNum;
        System.out.println("kVar = " + kVar);
        
        if (aNum % 2 == 0) {
            System.out.println("El numero es Par");
        } else {
            System.out.println("El numero es Impar");
        }
        
        if (bNum % 2 == 0) {
            System.out.println("El numero es Par");
        } else {
            System.out.println("El numero es Impar");
        }
        
        var edad = 30;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }
        */
        
        /*
        // Operador condicional AND "&&"
        var valorA = 7;
        var valorMinimo = 0; // rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA < 10;
        
        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        
        
        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) {
            System.out.println("El padre pede asistir al juego de su hijo");
        } else {
            System.out.println("El padre no puede asistir al juego de su hijo");
        }
        */
        /*
        // Operador ternario
        var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        // Es un operador compuesto por tres partes y separadas por los simbolos "?" ":"
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);
        */    
        /*
        var x = 5;
        var y = 10;        
        var z = ++x + y--; // En este caso veremos que a x se le sumara 1 y se sumara a y y luedo a y se le restara uno.
        System.out.println("z = " + z);
        // osea: priemro se realiza el incrememto de 'x', luego se suman '++x + y'
        // y luego se realiza el decremento a y
        
        
        var solucionAritmetica = 4 + 5 * 6 / 3; //El resultado sera 14 ya que el orden de la prioridad de los 
        // operadores primero se haran las operaciones de multiplicacion de y de division, y luego
        // se realizara la suma.
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3; // en este caso se evaluara primero el parentesis
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        */
        
        
        
        
        
        
        
        
    }
}
