# Escribir un programa que pueda listar todas las carpetas 
# y archivos del cwd por separado

import os,pprint

tamaño = os.path.getsize(r'Archivos\Clase5\texto_ejemplo.txt')

print(f'El tamaño del archivo "texto_ejemplo" es de: {tamaño}')
path = os.getcwd()
listado = os.listdir(path)
pprint.pprint(listado)

listaArchivos = []
listaCarpetas = []
for i in listado:
    #if i[-4] == '.' or i[-3] == '.':
    #if os.path.isfile(i):
    if not os.path.isdir(i):
        listaArchivos.append(i)
    else:
        listaCarpetas.append(i)
print('ARCHIVOS:')
pprint.pprint(listaArchivos)
print('CARPETAS:')
pprint.pprint(listaCarpetas)