# Ejercicio 3: Calcular estación del año
# Pedir al usuario que ingrese un mes del año, el valor
# debe ser entre 1 y 12, luego le decimos en que estación del
# año esta.
# Verano (21/12 al 21/3): 1, 2, 3
# Otoño (21/3 al 21/06): 4, 5, 6
# Invierno (21/06 al 21/09): 7, 8, 9
# Primavera (21/09 al 21/12): 10, 11, 12

mes = int(input("Ingrese el numero del mes: "))
estacion = None
if 1 <= mes <= 3:
    estacion = "Verano"
elif 4 <= mes <= 6:
    estacion = "Otoño"
elif 7 <= mes <= 9:
    estacion = "Invierno"
elif 10 <= mes <= 12:
    estacion = "Primavera"

print(f'El mes {mes} se encuentra en la estación {estacion}')
