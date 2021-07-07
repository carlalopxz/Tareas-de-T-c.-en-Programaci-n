# Escribir un programa con una opción para leer las primeras n líneas de un archivo 
# y otra opción para leer las últimas n líneas de un archivo.

import os 
nombreArchivo = r'Archivos\Clase3\texto_ejemplo.txt'
if os.path.exists(nombreArchivo):
    print('Archivo abierto')
    openFile = open(nombreArchivo,'r')
else:
    print('Archivo no encontrado')
readArchivo = openFile.readlines()
openFile.close()

numero_lineas = int(input('Digame la cantidad de lineas a leer: '))
if numero_lineas > 0:
    for i in range(numero_lineas):
        print(f'Linea numero {i}: {readArchivo[i]}')
    star = -(numero_lineas)
    for i in range(star,0):
        print(f'Linea numero {i}: {readArchivo[i]}')
print('Archivo cerrado')