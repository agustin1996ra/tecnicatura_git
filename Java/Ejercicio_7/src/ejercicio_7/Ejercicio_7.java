/* Ejercicio 7
  Una compañía de venta de autos usados, paga a su personal de 
  ventas un salario de $1000 mensuales mas una comisión de $150
  por cada auto vendido, más el 5% del valor de la venta por
  cada auto. Cada mes el capturista de la empresa ingresa en 
  la computadora los datos pertinentes.

  Hacer un programa que calcule e imprima el salario mensual
  de un vendedor dado.
  
  El salario de 1000 lo vamos a manejar como un dato constante,
  para asignarlo debemos usar la palabra reservada "final".
 */
package ejercicio_7;

import java.util.Scanner;


public class Ejercicio_7 {

    
    public static void main(String[] args) {
        final int salarioBase;
        salarioBase = 1000;
        double salarioComision = 0;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca el numero de autos que vendio el empleado: ");
        int nAutos = Integer.parseInt(entrada.nextLine());
        for (int i = 1; i < nAutos+1; i++) {
            System.out.println("Introduzca el monto de venta del auto "+i);
            double montoVenta = Double.parseDouble(entrada.nextLine());
            salarioComision = salarioComision +  150 + (montoVenta * 0.05);
        }
        double salarioTotal = salarioBase + salarioComision;
        System.out.println("El salario total del empleado es: $"+salarioTotal);
    }
    
}
