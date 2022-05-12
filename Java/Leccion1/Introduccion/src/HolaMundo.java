
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
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; // indicamos a Jaca la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        
        
    }
}
