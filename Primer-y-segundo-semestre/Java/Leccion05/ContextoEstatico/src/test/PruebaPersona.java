package test;

import domain.Persona;

public class PruebaPersona {
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Agustin");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Gabriel");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        // this.contador = 10; // No se puede referenciar desde un contexto estatico
        PruebaPersona personaP1 = new PruebaPersona();
        System.out.println(personaP1.getContador());
    }
    
    static public void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}

