#Ejercicio3.Escribir un programa que pueda contar el número de líneas/renglones en un archivo de texto.

import os 
nombreArchivo = 'Tareas-de-T-c.-en-Programaci-n\Archivos\Clase2\TextoEjemplo.txt'
if os.path.exists(nombreArchivo):
    print('Archivo abierto')
    archivoAbierto = open(nombreArchivo,'r')
else:
    print('archivo no encontrado')
contenido = archivoAbierto.readlines()
archivoAbierto.close()
    
print(f'Hay {len(contenido)} renglon/es' )
