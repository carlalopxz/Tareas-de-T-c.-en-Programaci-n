#Ejercicio2.Escribir un programa que pueda agregar texto a un archivo y luego mostrarlo.
#El archivo se puede llamar como quieran.

import os 
nombreArchivo = r'Archivos\Clase2\texto_ejemplo.txt'
if os.path.exists(nombreArchivo):
    print('Archivo abierto')
    archivoAbierto = open(nombreArchivo,'a')
else:
    print('Archivo creado')
    archivoAbierto = open(nombreArchivo,'a')
archivoAbierto.write("Texto de ejemplo\n")
archivoAbierto.close()
archivoAbierto = open(nombreArchivo,'r')
contenido = archivoAbierto.read()
archivoAbierto.close()
print(contenido)
print('Archivo cerrado')