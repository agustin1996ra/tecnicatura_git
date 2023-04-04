var nombre = 'José';
var apellido = 'Montes';
var nombreCompleto = nombre + ' ' + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Agustin' + ' ' + 'Rodriguez';
console.log(nombreCompleto2);
// En las concatenaciones se lee de izq a derecha
var juntos = nombre + 219;
console.log(juntos);
juntos = nombre + 78 + 17;
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);
juntos = nombre + (78 + 17);
console.log(juntos);

nombre += apellido;
console.log(nombre);
