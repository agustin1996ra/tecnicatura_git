/* Ejercicio 5
Hacer un programa que calcule e imprima la suma de 
tres calificaciones

Pedir las calificaciones al usuario, crear un proyecto nuevo llamado
Ejercicio 5.

*/
package ejercicio_5;

import java.util.Scanner;


public class Ejercicio_5 {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca la primera calificación: ");
        double c1 = Double.parseDouble(entrada.nextLine());
        System.out.println("Introduzca la segunda calificación: ");
        double c2 = Double.parseDouble(entrada.nextLine());
        System.out.println("Introduzca la tercera calificación: ");
        double c3 = Double.parseDouble(entrada.nextLine());
        var resultado = c1 + c2 + c3;
        System.out.println("El resultado de la suma de las tres calificaciones es: " + resultado);
        
    }
    
}
