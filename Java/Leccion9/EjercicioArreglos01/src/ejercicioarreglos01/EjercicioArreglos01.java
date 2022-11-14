/*
Ejercicio 1: Leer 5 números, guardarlos en una arreglo y mostrarlos en el mismo
orden introducidos.
 */
package ejercicioarreglos01;

import java.util.Scanner;

public class EjercicioArreglos01 {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int [5];
        for (int i = 0; i < 5; i++) {
            System.out.println("Introduzca un numero: ");
            int numero = Integer.parseInt(entrada.nextLine());
            numeros[i] = numero;
        }
        System.out.println("\nLos numeros introducidos son:");
        for (int i = 0; i < 5; i++) {
            System.out.println("Numnero "+i+": "+numeros[i]);
        }
        
    }
    
}
