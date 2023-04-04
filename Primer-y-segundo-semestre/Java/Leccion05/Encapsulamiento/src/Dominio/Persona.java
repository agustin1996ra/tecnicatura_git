
package Dominio;


public class Persona {
    // Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    // Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public String getNombre() {
        return this.nombre;
    }
    
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }
    
    public double getSueldo() {
        return this.sueldo;
    }
    
    public void setEliminado(boolean eliminado){
        this.eliminado = eliminado;
    }
    
    public boolean isEliminado(){
        return eliminado;
    }
    
    public String toString(){ // Convierte en una cadena cada atributo
        return "Persona {nombre= "+this.nombre+
                ", sueldo= "+this.sueldo+
                ", eliminado= "+this.eliminado+" }";
    }
    
}
