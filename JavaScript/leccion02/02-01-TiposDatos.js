/* Tipos de Datos en JavaScript
La sintaxis en lo que es comentarios es muy similar
a la de java, realmente diríamos que es idéntica
*/
var nombre = "Agustin";  // Tipo str
console.log(nombre);
console.log(typeof nombre);
nombre = 7;
console.log(nombre);
console.log(typeof nombre);
nombre = 12.3;
console.log(nombre);
console.log(typeof nombre);

var numero = 3000;  // Tipo numérico
console.log(numero);

var objeto = {
    nombre : "Agustin",
    apellido : "Rodriguez",
    telefono : "2944560554"
}

console.log(objeto);

// Tipo de dato booleano
var bandera = true;
console.log(bandera);
console.log(typeof bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo")
console.log(simbolo);
console.log(typeof simbolo);


// Tipo de dato clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona)


