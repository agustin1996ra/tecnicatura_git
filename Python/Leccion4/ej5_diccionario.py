# La tarea consiste en ingresar elementos al diccionario llamado
# seleccionArgentina, lo elementos a ingresar deben ser como mínimo 4,
# estos elementos son los jugadores con su número de camiseta, nombre,
# apellido, edad, altura, precio y posición de juego, por supuesto ver
# el video anterior

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    2: {'Nombre': 'Juan Foyth', 'Edad': 24, 'Altura': 1.87, 'Precio': '25 Millones', 'Posicion': 'Lateral Derecho'},
    3: {'Nombre': 'Nicolas Tagliafico', 'Edad': 30, 'Altura': 1.72, 'Precio': '11 Millones', 'Posicion': 'Lateral Izquierdo'},
    4: {'Nombre': 'Gonzalo Montiel', 'Edad': 25, 'Altura': 1.76, 'Precio': '14 millones', 'Posicion': 'Lateral Derecho'},
    5: {'Nombre': 'Alexis Mac Alister', 'Edad': 23, 'Altura': 1.74, 'Precio': '16 Millones', 'Posicion': 'Mediocentro Ofensivo'}
}

for key, value in seleccionArgentina.items():
    print(f'camiseta: {key}  {value}')

