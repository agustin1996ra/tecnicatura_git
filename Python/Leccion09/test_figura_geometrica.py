from Cuadrado import Cuadrado
from Rectangulo import *

cuadrado1 = Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'El area del cuadrado es: {cuadrado1.calcular_area()}')

print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(4, 3, "Rojo")
print(rectangulo1)

rec = Rectangulo2(4,3,"Amarillo")
print(rec)