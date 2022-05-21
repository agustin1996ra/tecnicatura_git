// Ejercicio 2 
// Hacer un programa que calcule e imprima el salario de un empleado
// a partir de sus horas semanales trabajdas y su salario por hora
package ejercicio_2;

import java.util.Scanner;


public class Ejercicio_2 {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el numero de horas semanales: ");
        int horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el valor de la hora: ");
        double valorHoras = Double.parseDouble(entrada.nextLine());
        double salarioSemanal = horasSemanales * valorHoras;
        System.out.println("\nEl salario semanal del tabajador sera:  $ "+ salarioSemanal);
    }
    
    
}
