import os,zipfile
from random import randint

#ABRIR ARCHIVO CON LAS PREGUNTAS
nombre_preguntas = 'preguntas.txt'
if os.path.exists(nombre_preguntas):
    archivo_abierto = open(nombre_preguntas,encoding='utf-8')
    print('ARCHIVO ABIERTO')
    archivo = archivo_abierto.readlines()
    archivo_abierto.close()
else:
    print('Archivo no encontrado')

#CREACION DE CARPETAS

directorio = "cuestionarios"
try:
    os.mkdir(directorio)
except OSError:
    print("La creación del directorio %s falló" % directorio)
else:
    print("Se ha creado el directorio: %s " % directorio)

directorio = "respuestas"
try:
    os.mkdir(directorio)
except OSError:
    print("La creación del directorio %s falló" % directorio)
else:
    print("Se ha creado el directorio: %s " % directorio)

#COPIAR CADA PREGUNTA COMO UN ELEMENTO DE UNA NUEVA LISTA
lista = []
for i in range(0,len(archivo),5):
    lista.append(archivo[i:i+5])


#ELEGIR 10 PREGUNTAS AL AZAR DE LA LISTA.
random_preg = []
orden_preg = []
for x in range(0,20,1):
    for i in range(0,10,1):
        while True:
            num_random = randint(0,19)
            if num_random not in random_preg:
                random_preg.append(num_random)
                break
    orden_preg.append(random_preg)
    random_preg = []

#CREACION DE ARCHIVOS 

x = 0
for k in range(1,21):
    archivo = open(f'cuestionarios\\cuestionario{k}.txt','w',encoding='utf-8')
    for j in orden_preg[x]:
        for i in lista[j]:
            archivo.write(i + "\n")
    archivo.close()
    x += 1

#COPIAR RESPUESTAS

archivo = open(f'respuestas.txt')
respuestas = archivo.readlines()
archivo.close()

respuestasLista = []
for i in range(len(orden_preg)):
    for j in orden_preg[i]:
        respuestasLista.append(respuestas[j])
indice = 0
for x in range(1,21):
    archivo = open(f'respuestas\\respuestas{x}.txt','w')
    for j in respuestasLista[indice:indice+10]:
        archivo.write(j + '\n') 
    archivo.close()
    indice += 10

#COMPRIMIR EN ARCHIVO ZIP

archivos_Cuestionarios = r'cuestionarios.zip'
nombreZip = zipfile.ZipFile(archivos_Cuestionarios, 'w')
for i in range(1,21,1):
    nombreZip.write(f'cuestionarios\\cuestionario{i}.txt')
nombreZip.close()

archivos_Respuestas = r'respuestas.zip'
nombreZip = zipfile.ZipFile(archivos_Respuestas, 'w')
for i in range(1,21,1):
    nombreZip.write(f'respuestas\\respuestas{i}.txt')
nombreZip.close()