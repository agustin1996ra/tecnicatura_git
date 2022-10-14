/*
 Ejercicio 4: Pedir números hasta que se teclee uno negativo
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner.
Luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;
import javax.swing.JOptionPane;
import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int contador = 0;
        while (true) {
            System.out.println("Ingrese un numero: ");
            int numero = Integer.parseInt(entrada.nextLine());
            if (numero < 0){
                break;
            }
            contador++;
            
        }
        System.out.println("La cantidad de números ingresados es: "+ contador);
        
        contador = 0;
        
        while (true) {            
            int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
            if (numero < 0){
                break;
            }
            contador++;
        }
        
        JOptionPane.showMessageDialog(null, "La cantidad de número ingresados es " + contador);
        
    }
}
