/*
Ejercicio 2: Leer 5 números, guardarlos en una arreglo y mostrarlos en el orden 
inverso al que fueron introducidos.
*/
package ejercicioarreglos02;

import java.util.Scanner;

public class EjercicioArreglos02 {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int [5];
        for (int i = 0; i < 5; i++) {
            System.out.println("Introduzca un numero entero: ");
            int numero = Integer.parseInt(entrada.nextLine());
            numeros[i] = numero;
        }
        
        for (int i = 4; i >= 0; i--) {
            System.out.println("Numero "+i+": "+numeros[i]);
        }
    }
    
}
