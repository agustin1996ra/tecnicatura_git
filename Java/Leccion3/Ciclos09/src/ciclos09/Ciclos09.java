/*
Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si 
la fecha es correcta. Suponiendo que todos los meses son de 30 
días.
 */
package ciclos09;
import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos09 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca el día: ");
        int dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Introduzca el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Introduzca el año: ");
        int anio = Integer.parseInt(entrada.nextLine());
        if ((dia > 0)&&(dia <= 30)) {
            if ((mes > 0)&&(mes <= 12)) {
                if ((anio > 0)&&(anio <= 2022)) {
                    System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else {
                    System.out.println("Fecha incorrecta, año incorrecto.");
                }
            }
            else {
                System.out.println("Fecha incorrecta, mes incorrecto.");
            }
        }
        else {
            System.out.println("Fecha incorrecta, día incorrecto.");
        }
        
        
        dia = Integer.parseInt(JOptionPane.showInputDialog("Introduzca el día: "));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
        anio = Integer.parseInt(JOptionPane.showInputDialog("Introduzca el año: "));
        if ((dia > 0)&&(dia <= 30)) {
            if ((mes > 0)&&(mes <= 12)) {
                if ((anio > 0)&&(anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto.");
                }
            }
            else {
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto.");
            }
        }
        else {
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto.");
        }
                
        
    }
    
}
