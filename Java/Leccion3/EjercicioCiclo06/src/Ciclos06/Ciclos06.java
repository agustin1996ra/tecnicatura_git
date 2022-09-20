/*
Ejercicio 6: Pedir números hasta que se teclee un 0,
mostrar la suma de todos los números introducidos.
*/
package Ciclos06;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos06 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        
        do {            
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        } while (numero != 0);
        
        System.out.println("La suma de los numeros ingresados es: "+suma);
        
        suma = 0;
        
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma += numero;
        } while (numero != 0);
        
        JOptionPane.showMessageDialog(null, "La suma de los números ingreados es: "+suma);
        
        
    }
    
}
