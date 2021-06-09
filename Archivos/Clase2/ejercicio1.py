#Ejercicio1.Escribir un programa que pueda leer un archivo de texto entero. 
#Para este ejercicio el archivo se llama TextoEjemplo.txt
import os
#Nombre del archivo
nombreArchivo = 'TextoEjemplo.txt'
if os.path.exists(nombreArchivo):#Revisamos que exista
    archivoAbierto = open(nombreArchivo,'r')#1.Abrimos el archivo
else:
    print('Archivo no encontrado')
contenido = archivoAbierto.read() #2.Leemos el archivo
archivoAbierto.close() #3.Lo cerramos.
print(contenido)