/*
 Ejercicio 7:
Pedir números hasta que se introduzca uno negativo y calcular la media
 */
package ejerciciociclos07;
import java.util.Scanner;
import javax.swing.JOptionPane;


public class EjercicioCiclos07 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int suma = 0, numero, contador = 0;
        do {            
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero > 0) {
                suma += numero;
                contador++;
            }
        } while (numero > 0);
        var media = suma / contador;
        System.out.println("La media de los números ingresados es: "+media);
        
        
        
        suma = 0;
        contador = 0;
        do {            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            if (numero > 0) {
                suma += numero;
                contador++;
            }
        } while (numero > 0);
        media = suma / contador;
        JOptionPane.showMessageDialog(null, "La media de los números ingresados es: "+media);
    }
    
}
