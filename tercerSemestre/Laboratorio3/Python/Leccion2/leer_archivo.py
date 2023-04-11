
archivo = open('./archivos/prueba.txt', 'r', encoding='utf8')
# print(archivo.read())
# print(archivo.read(5))  # Esto lee los primeros 5 caracteres del archivo
# print(archivo.read(15))  # Esto lee los siguientes caracteres del archivo
# print(archivo.readline())
# print(archivo.readline())

# Vamos a iterar el archivo. Cada una de las lineas
# for linea in archivo:
#     print(linea)
# print(archivo.readlines())  # Esto genera una lista


# Anexamos información, copiamos a otro
archivo2 = open('./archivos/copia.txt', 'w', encoding='utf8')  # Las letras son: 'r', 'a', 'w', 'x'
"""
la letra r es para leer, la a es para anexar, w es para escribir (eliminando lo anterior), la letra x es para
crear un archivo, t para texto, b para binarios, w+ sirve para escribir y leer, r+ para leer y escribir
"""
archivo2.write(archivo.read())
archivo2.close()
archivo.close()

print('Se ha terminado el proceso de leer y coppiar archivos')