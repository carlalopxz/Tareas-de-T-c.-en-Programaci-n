# Escribir un programa que lea los datos de un archivo de texto, que transforme cada línea en un diccionario 
# y los añada a una lista. Luego recorrer las personas de la lista y para cada una mostrar todos sus valores 
# de manera que sean fáciles de leer. Las claves de cada diccionario serán id, nombre, apellido y nacimiento.
# El archivo de texto se denominará agenda.txt y tendrá el siguiente contenido:
# agenda.txt

#Ejemplo.
#agenda = []
#agenda[{'id':'1','nombre':'Carlos','apellido':'Perez','nacimiento':'05/01/1989'},{},{},{}]
"""
#######
ID: 1
Nombre: Carlos
Apellido: Perez
Nacimiento: 05/01/1989
#######
ID: 2
....
"""
import os,pprint
archivoAbierto = open(r'Archivos\Clase5\agenda.txt')
contenido = archivoAbierto.readlines()
archivoAbierto.close()
agenda = []
for linea in contenido:
    contacto = {}
    lineaSplit = linea.split(';')
    contacto['id'] = lineaSplit[0]
    contacto['nombre'] = lineaSplit[1]
    contacto['apellido'] = lineaSplit[2]
    contacto['nacimiento'] = lineaSplit[3].strip('\n')
    #contacto['id'],contacto['nombre'],contacto['apellido'],contacto['nacimiento'] = lineaSplit
    agenda.append(contacto)
for contacto in agenda:
    print(f"Contacto{contacto['id']}".center(30,'#'))
    print(f"ID: {contacto['id']}")
    print(f"Nombre: {contacto['nombre']}")
    print(f"Apellido: {contacto['apellido']}")
    print(f"Nacimiento: {contacto['nacimiento']}")
