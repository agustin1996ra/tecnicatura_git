class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # Para indicar un metodo estatico se usa un decorador
    @staticmethod
    def metodo_estatico():  # Metodo estatico, se asocia a la clase
        print(MiClase.variable_clase)


print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# Se puede crear una variable de clase, fuera del cuerpo de la clase
MiClase.variable_clase2 = 'Valor de variable de clase 2'
# Las variables pueden ser llamadas desde la clase en si y los objetos/instancias
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)
MiClase.metodo_estatico()

# Una clase se carga en memoria cuando de instancia un objeto
