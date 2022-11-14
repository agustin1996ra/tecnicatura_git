/*
Uso de la palabra final 
Esta palabra tiene diferentes significados dependiendo donde 
se aplique:
Variables: Evita cambiar el valor que almacena la variable
Métodos: Evita que se modifique la definición o el comportamiento 
de un método desde una subclase (hija)

clases; Evita que se creen clases hijas

Otra caracteristicas es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estático, para convertir una variable
en una constante, es decir que no se puede modificar si valor, 
el ejemplo de esto es la clase Math en la cual todos sus atributos 
son de tipo static y final, es por esto que la variable pi se conoce como una
constante.
 */
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        // miDni = 20312321; No se puede modificar
        // Persona.CONSTANTE_AQUI = 9; no se modifica
        
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        // persona1 = new Persona(); No se puede asignar una nueva referencia 
        persona1.setNombre("Agustin Rodriguez");
        System.out.println("persona1 nombre: "+persona1.getNombrte());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: "+ persona1.getNombrte());
    }
}
