/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificaciones
mostradas a continuación.
La formula es: Volumen = ancho * alto * profundidad
*/
package Caja;


public class PruebaCaja {
    public static void main(String[] args) {
        int ancho = 4;
        int alto = 3;
        int profundidad = 5;

        Caja caja1 = new Caja(ancho, alto, profundidad);
        int volumen = caja1.calcularVolumen();
        System.out.println("El volumen de la caja es: "+ volumen);

        Caja caja2 = new Caja();
        caja2.ancho = 2;
        caja2.alto = 3;
        caja2.profundo = 4;
        int volumen2 = caja2.calcularVolumen();
        System.out.println("El volumen de la caja es: "+ volumen2);
        
    }
}
