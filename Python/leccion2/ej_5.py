# Ejercicio 5: Sistema de calificaciones
# El objetivo del programa será crear un sistema de calificaciones
# de la siguiente manera:
# Le pedimos al usuario que ingrese un valor de 0 al 10
# Luego si ingreso 9 o 10 imprimimos A
# Entre 8 y menor a 9 imprimimos B
# Entre 7 y menor a 8 imprimimos C
# Entre 6 y menor a 7 imprimimos D
# Entre 0 y menor a 6 imprimimos F
# De lo contrario el valor ingresado es incorrecto

nota = None
nota_numerica = float(input("Ingrese la nota que desea convertir: "))

if 9 <= nota_numerica <= 10:
    nota = "A"
elif 8 <= nota_numerica < 9:
    nota = "B"
elif 7 <= nota_numerica < 8:
    nota = "C"
elif 6 <= nota_numerica < 7:
    nota = "D"
elif 0 <= nota_numerica < 6:
    nota = "F"
else:
    nota = "ERROR!: el valor ingresado es incorrecto"

print(f'La nota numerica {nota_numerica} equivale la letra {nota}')
