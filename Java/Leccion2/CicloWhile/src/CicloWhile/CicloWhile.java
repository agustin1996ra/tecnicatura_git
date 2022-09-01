
package CicloWhile;


public class CicloWhile {
    public static void main(String[] args) {
        var conteo = 0; // Inferencia de titpos
        while(conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++;  // Aumento en uno la variable
        }
        
        var contador = 0;
        do {            
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);
        
        for(var contando = 0; contando < 7; contando++) {
            System.out.println("contando = " + contando);
        }
        // break 
        for(var contando = 0; contando < 7; contando++) {
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break; // se interrumpe la ejecucion del ciclo
            }
        }
        
        // continue
        for(var contando = 0; contando < 7; contando++) {
            if(contando % 2 == 0){
                continue; // Continue, pero con la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }
        
        
        // Etiquetas labels
        inicio:
        for(var con = 0; con < 7; con++) {
            if(con % 2 == 0){
                System.out.println("con = " + con);
                break inicio;
            }
        }
        
        inicio2:
        for(var contando = 0; contando < 7; contando++) {
            if(contando % 2 == 0){
                continue inicio2; // Continue, pero con la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }
        
        
    }
}
