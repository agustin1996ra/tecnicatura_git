/*
Ejercicio 8: Pedir un número N, y mostrar todos los números
del 1 al N.
*/
package ciclos08;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos08 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextLine());
        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
        
    }
    
}
