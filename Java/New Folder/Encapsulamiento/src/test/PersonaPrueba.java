
package test;

import Dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        // Modificar a través de los métodos
        persona1.setNombre("Juan Ingnacio");
        //persona1.nombre = "Juan Ignacio"; ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); ya no se puede utilizar
        
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 esta eliminado: "+persona1.isEliminado());
        
        // Tarea Crear otro objeto de tipo Persona, asignar valores de manera inicial
        // y imprimir, luego modificar sis valores y volver a imprimir
    }
}
