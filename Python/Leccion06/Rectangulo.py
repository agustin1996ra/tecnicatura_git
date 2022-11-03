class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér 2 atributos:
    altura y base. El nombre del método será calcular area utilizando
    la formula: area = base * altura. Pero la base y la altura deben ser
     ingresadas por el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self._altura = altura
        self._base = base

    def calcular_area(self):
        return self._altura * self._base


# Rectángulo1
altura1 = float(input('Ingrese la altura del rectángulo 1: '))
base1 = float(input('Ingrese la base del rectángulo 1: '))
r1 = Rectangulo(altura1, base1)
area1 = r1.calcular_area()
print(f'El rectángulo 1 de altura {altura1} y base {base1},')
print(f'tiene área {area1}\n')

# Rectángulo2
altura2 = float(input('Ingrese la altura del rectángulo 2: '))
base2 = float(input('Ingrese la base del rectángulo 2: '))
r2 = Rectangulo(altura2, base2)
area2 = r2.calcular_area()
print(f'El rectángulo 1 de altura {altura2} y base {base2},')
print(f'tiene área {area2}\n')

# Rectángulo3
altura3 = float(input('Ingrese la altura del rectángulo 3: '))
base3 = float(input('Ingrese la base del rectángulo 3: '))
r3 = Rectangulo(altura3, base3)
area3 = r3.calcular_area()
print(f'El rectángulo 1 de altura {altura3} y base {base3},')
print(f'tiene área {area3}\n')
