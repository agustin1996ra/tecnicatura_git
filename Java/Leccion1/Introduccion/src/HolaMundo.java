
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
        // Conversión de tipos primitivos (parte dos)
        /*
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter");
        var entrada = new Scanner(System.in);
        fraseChar = entrada.nextLine().charAt(0); // por mas que pongamos una cadena, solo tomara el carater en el indice especificado.
        System.out.println("fraseChar = " + fraseChar);
        */
        
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
        
        
    }
}
