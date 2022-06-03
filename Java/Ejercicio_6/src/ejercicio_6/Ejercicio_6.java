/* Ejercicio 6
 Guillermo tiene N dólares. Luis tiene la mitad de lo que posee
 Guillermo. Juan tiene la mitad de lo que poseen Luis y Guillermo juntos.
 Hacer un programa que calcule e imprima la cantidad de dinero que
 tienen entre los tres.
 */
package ejercicio_6;

import java.util.Scanner;


public class Ejercicio_6 {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca la cantidad de dólares que tiene Guillermo: ");
        Double dolaresG = Double.parseDouble(entrada.nextLine());
        var resultado = dolaresG * 2.25;
        System.out.println("El total de dolares que tienen los tres es: U$D"+resultado);
    }
    
}
