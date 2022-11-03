class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # Decorador
    def nombre(self):
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


persona1 = Persona2('Agustin', 'Rodriguez', 26)
print(persona1.nombre)  # llamamos al método getter
persona1.nombre = 'Juan Pablo'
print(persona1.nombre)
print(persona1.mostrar_detalles())
