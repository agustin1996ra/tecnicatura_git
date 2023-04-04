/*
Ejercicio 3: Leer 5 números por teclado, almacenarlos en un arreglo y a 
continuación realizar la media de los número positivos, la media de los
negativos y contar el números de ceros.
*/

package ejercicioarreglos03;

import java.util.Scanner;

public class EjercicioArreglos03 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int [5];
        int positivos = 0;
        int negativos = 0;
        int ceros = 0;
        double suma_positivos = 0;
        double suma_negativos = 0;
        
        for (int i = 0; i < 5; i++) {
            System.out.println("Introduzca un numero: ");
            int numero = Integer.parseInt(entrada.nextLine());
            numeros[i] = numero;
        }
        
        for (int i = 0; i < 5; i++) {
            if (numeros[i] > 0) {
                positivos++;
                suma_positivos += numeros[i];
            }
            else if (numeros[i] < 0) {
                negativos++;
                suma_negativos += numeros[i];
            }
            else {
                ceros++;
            }
        }
        
        if (positivos != 0) {
            double media_positivos = suma_positivos / positivos;
            System.out.println("La media de los positivos es: "+ media_positivos);
        }
        if (negativos != 0) {
            double media_negativos = suma_negativos / negativos;
            System.out.println("La media de los negativos es: "+ media_negativos);
        }
        if (ceros != 0) {
            System.out.println("Los ceros en el arreglo son: "+ ceros);
        }
        
    }
    
}
