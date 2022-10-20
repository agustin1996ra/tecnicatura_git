class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la fórmula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    """

    def __init__(self, ancho, altura, profundidad):
        self._ancho = ancho
        self._altura = altura
        self._profundidad = profundidad

    def calcular_volumen(self):
        volumen = self._ancho * self._altura * self._profundidad
        return volumen


ancho1 = float(input('Introduzca el ancho del cubo: '))
altura1 = float(input('Introduzca la altura del cubo: '))
profundidad1 = float(input('Introduzca la profundidad del cubo: '))
cubo = Cubo(ancho1, altura1, profundidad1)
volumen1 = cubo.calcular_volumen()
print(f'El cubo de ancho {ancho1}, altura {altura1} y profundidad {profundidad1},')
print(f'tiene un volumen {volumen1}')
