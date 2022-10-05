class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Agustin', 'Rodriguez', 26)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido}  Su edad es: {persona2.edad}')
print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido}  Su edad es: {persona1.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}  Su edad es: {persona1.edad}')

# Los atributos son: características
# Los métodos son: el comportamiento que va a tener los objetos (acciones)


