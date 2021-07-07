#Ejercicio8. Escribir un programa que pueda cargar, borrar o modificar personas del listado del ejercicio anterior.
"""agenda.txt
1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
"""
#Desea cargar un contacto nuevo?
#Id:
#Nombre:
#Apellido:
#Nacimiento:
#-Mostrar todos los contactos.

import os

nameFile = r'Archivos\Clase5\agenda.txt'

def generarAgenda(nameFile):
    #Abrimos Archivo
    if os.path.exists(nameFile):
        print('Archivo abierto')
        openFile = open(nameFile)
    else:
        print('Archivo no encontrado')
    contenido = openFile.readlines()
    openFile.close()
    #Creamos agenda
    agenda = []
    for linea in contenido:
        contacto = {}
        lineaSplit = linea.split(';')
        contacto['id'] = lineaSplit[0]
        contacto['nombre'] = lineaSplit[1]
        contacto['apellido'] = lineaSplit[2]
        contacto['nacimiento'] = lineaSplit[3].strip('\n')
        agenda.append(contacto)
    return agenda
def mostrarAgenda(agenda):
    #Mostramos la agenda
    for contacto in agenda:
        print(f"Contacto {contacto['id']}".center(30,'#'))
        print(f"ID: {contacto['id']}")
        print(f"Nombre: {contacto['nombre']}")
        print(f"Apellido: {contacto['apellido']}")
        print(f"Nacimiento: {contacto['nacimiento']}")
#Agregar contactos a la agenda
def agregarContacto(agenda):
    nombre = input('Nombre: ').capitalize()
    apellido = input('Apellido: ').capitalize()
    nacimiento = input('Nacimiento: ')
    id = str(int(agenda[-1]['id']) + 1)
    openFile = open(nameFile,'a')
    openFile.write(f'\n{id};{nombre};{apellido};{nacimiento}')
    openFile.close()
    agenda = generarAgenda(nameFile)
    mostrarAgenda(agenda)
#Borrar contactos y guardar la agenda nueva con el contacto borrado 
def borrarContacto(agenda):
    id_a_borrar = input('Ingrese el ID: ')
    #nombre_para_borrar = input('Ingrese un nombre: \n').capitalize()
    for contacto in agenda:
        if id_a_borrar in contacto.values() :
            indice_contacto = agenda.index(contacto)
            opcion_borrar = input(f'Desea borrar contacto: \n A) SI \n B) NO \n' ).lower()
            if opcion_borrar == 'si' or opcion_borrar == 'a':
                del agenda[indice_contacto]
                guardarAgenda(agenda)
                print('Contacto borrado')
                return
            else:
                break
    print('Nombre de contacto no encontrado')
def guardarAgenda(agenda):
    listaParaArchivo = []
    for contacto in agenda:
        cadena = []
        #contacto['id'] +';'+ contacto['nombre']+';'+ contacto['apellido'] +';'+ contacto['nacimiento']
        for dato in contacto.values():#{'id':2,'nombre':'Manuel','apellido':'Heredia','nacimiento':26/12/1973}
            cadena.append(dato)
        #cadena = ['2','Manuel','Heredia','26/12/1973']
        cadena = ';'.join(cadena)
        #cadena = '2;Manuel;Heredia;26/12/1973'
        listaParaArchivo.append(cadena)
    cadenaParaArchivo = '\n'.join(listaParaArchivo)
    #listaParaArchivo = '2;Manuel;Heredia;26/12/1973\n2;Manuel;Heredia;26/12/1973\n2;Manuel;Heredia;26/12/1973\n2;Manuel;Heredia;26/12/1973'
    archivoAbierto = open(r'Archivos\Clase5\agenda.txt','w')
    archivoAbierto.write(cadenaParaArchivo)
    archivoAbierto.close() 
def modificarAgenda(agenda):
    id = int(input('Ingrese el ID del contacto que desea modificar: '))
    print(f'Contacto: {agenda[id-1]}')
    opcion = input('¿Que desea modificar? Nombre - Apelido - Nacimiento \n').lower()
    if opcion == 'nombre':
        nombre = input('Ingrese el nombre nuevo: ')
        for contacto in range(len(agenda)):
            if contacto == id:
                contacto_modificar = agenda[id-1]
                contacto_modificar['nombre'] = nombre
                guardarAgenda(agenda)
                print('CONTACTO MODIFICADO')
    if opcion == 'apellido':
        apellido = input('Ingrese apellido nuevo: ')
        for contacto in range(len(agenda)):
            if contacto == id:
                contacto_modificar = agenda[id-1]
                contacto_modificar['apellido'] = apellido
                guardarAgenda(agenda)
                print('CONTACTO MODIFICADO')
    if opcion == 'nacimiento':
        nacimiento = input('Ingrese el nacimiento: ')
        for contacto in range(len(agenda)):
            if contacto == id:
                contacto_modificar = agenda[id-1]
                contacto_modificar['nacimiento'] = nacimiento
                guardarAgenda(agenda)
                print('CONTACTO MODIFICADO')
           
#Llamar a las funciones 
agenda = generarAgenda(nameFile)

#Menu de opciones 
while True:
    opcion = input('Desea:\n A) Agregar contactos \n B) Borrar contacto\n C) Modificar agenda \n D) Salir\n ').lower()
    if opcion == 'a':
        agregarContacto(agenda)
        mostrarAgenda(agenda)
    if opcion == 'b':
        borrarContacto(agenda)
        mostrarAgenda(agenda)
    if opcion == 'c':
        modificarAgenda(agenda)
        #mostrarAgenda(agenda)
    if opcion == 'd':
        break