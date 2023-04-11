# Manejo de contexto with: sintaxis simplificada, abre y cierra el archivo
import ManejoArchivos

with open('./archivos/prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# en el contexto de with lo que se ejecuta de manera automática son
# diferentes métodos: __enter__ este es el que abre el archivo
# ahora el siguiente método es el que cierra: __exit__

with ManejoArchivos.ManejoArchivo('./archivos/prueba.txt') as archivo:
    print(archivo.read())
    

