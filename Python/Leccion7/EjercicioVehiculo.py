"""
Definir una clase padre llamada Vehículo y dos clases hijas llamadas
Auto y Bicicleta, las cuales heredan de la clase padre Vehículo. La
clase padre debe tener los siguientes atributos y métodos:

    Vehículo(clase padre)
    - Atributos(color, ruedas)
    - Métodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehículo)
    - Atributos(velocidad )
    - Métodos(__init__(color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehículo)
    - Atributos(tipo(urbana/montaña/etc.)
    - Métodos(__init__(color, ruedas, tipo) y __str__())

Crear un objeto de cada clase
"""


class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'Vehículo [ Color: {self._color}, Ruedas: {self._ruedas}]'


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f'Auto [ Velocidad: {self._velocidad}]  {super().__str__()}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f'Bicicleta [ Tipo: {self._tipo} ] {super().__str__()}'


vehiculo1 = Vehiculo('rojo', 4)
print(vehiculo1)

auto1 = Auto('blanco', 4, 150)
print(auto1)

bicicleta1 = Bicicleta('amarilla', 2, 'montañas')
print(bicicleta1)
