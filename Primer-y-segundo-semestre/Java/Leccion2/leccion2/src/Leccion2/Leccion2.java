
package Leccion2;

import java.util.Scanner;


public class Leccion2 {
    public static void main(String[] args) {
        
        // Sentecia de control
//        var condicion = true;
//        if (condicion){
//            System.out.println("Condicion verdadera");
//        }
//        else{
//            System.out.println("Condicion falsa");
//        }
        
        // Ejercicio if/else
//        var numero = 2;
//        var numeroTexto = "Número desconocido";
//        if (numero == 1) {
//            numeroTexto = "Número uno";
//        }
//        else if (numero == 2) {
//            numeroTexto = "Número dos";
//        }
//        else if (numero == 3) {
//            numeroTexto = "Número tres";
//        }
//        else if (numero == 4) {
//            numeroTexto = "Número cuatro";
//        }
//        else{
//            numeroTexto = "Número no encontrado";
//        }
//        System.out.println("numeroTexto = " + numeroTexto);
        
        // Utilizamos else if para que el compilador, entienda que todas las
        // comprobaciones corresponden a una misma estructura, de esta manera
        // trabajara mucho menos.
        
        
        // Sentencia de control Switch
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite un número del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero){
            case 1:
                numeroTexto = "Número uno";
                break;
            case 2:
                numeroTexto = "Número dos";
                break;
            case 3:
                numeroTexto = "Número tres";
                break;
            case 4:
                numeroTexto = "Número cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}
