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


// Tipo de dato undefined
var x;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y)

// Tipo de dato array y empty string
var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos); // Preguntamos que tipo de dato es:

var z = '';
console.log(z); // Esto de refiere a que es una cadena vacia:
console.log(typeof z);
