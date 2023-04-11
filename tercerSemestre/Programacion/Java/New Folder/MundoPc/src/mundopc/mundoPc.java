package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPc {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 19); 
        Teclado tecladoHP = new Teclado("Bluethooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        // Creamos otros objetos diferentes
        Monitor monitorGamer = new Monitor("Gamer", 27); 
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
        Computadora computadoraVarias = new Computadora("Computadoras de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        
        Orden orden1 = new Orden(); // Incializamos vacio el arreglo
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarComputadora(computadoraVarias);
        
        // Tarea: crear mas objetos computadoras con todos sus elementos
        // completar una lista en el objeto orden1 que llegue a los 10 elementos
        // provar de esta maera los métodos al maximo rendimiento.
        
        
        
        
    }
}
