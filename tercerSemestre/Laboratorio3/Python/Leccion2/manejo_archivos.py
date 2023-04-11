# Al declarar una variable de esta forma creamos un archivo
try:
    archivo = open('./archivos/prueba.txt', 'w', encoding='utf8')  # la w viene de write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # Con esto se cierra el archivo
#  archivo.write('Todo perfecto!') este es un error
