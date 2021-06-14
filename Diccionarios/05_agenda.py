'''
Ejercicio.5.Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y 
números de teléfono. El programa nos dará el siguiente menú: 
1)Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se
encuentra, debe permitir ingresar el teléfono correspondiente.
2)Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres
comiencen por dicha cadena.
3)Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
4)Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.

print("\033[H\033[J")
'''

print('BIENVENIDO A SU AGENDA')
import pprint
agenda = {'Juani':1123942359, 'Mamá': 3454030985,'Rolando':1140272127,'Carina':1135642708,'May':1159555229}
while True:
    
    opcion = input('Elija una opcion para continuar: \n A) Añadir/modificar \n B) Buscar \n C) Borrar \n D) Listar \n E) Quiero salir \n').lower()

    def opcion_add_modificar():
        nombre_contacto = input('Ingrese un nombre: \n').capitalize()
        if nombre_contacto in agenda.keys():
            print(f'{nombre_contacto}:{agenda[nombre_contacto]}')
            opcion_modificar = input('Desea modificar el contacto: \n A) SI \n B) NO \n').lower()
            if opcion_modificar[0] != 'n':
                agenda[nombre_contacto] = int(input('Modifique el contacto: \n'))
                print(f'Contacto modifcado a: {agenda[nombre_contacto]}')
        else:
            opcion_add = input('¿Desea añadir el contacto? \n A) SI \n B) NO \n')
            if opcion_add[0] != 'n':
                agenda[nombre_contacto] = int(input('Ingrese el numero para agregar a la agenda\n'))
            print(agenda[nombre_contacto])
            print(agenda)

    def opcion_buscar():
        letra = input('Ingrese una letra: ').capitalize()
        lista_contactos = agenda.items()
        for contacto,numero in lista_contactos:
            if letra == contacto[0]:
                print(f'Los contactos con {letra} son {contacto} : {numero}')

    def opcion_borrar():
        nombre_para_borrar = input('Ingrese un nombre: \n').capitalize()
        if nombre_para_borrar in agenda.keys():
            opcion_borrar = input(f'Desea borar el nombre de {nombre_para_borrar}: \n A) SI \n B) NO \n' ).lower()
            if opcion_borrar == 'si':
                del agenda[nombre_para_borrar]
                print('Contacto borrado')
        else:
            print('No se encontro el contacto')

    def opcion_listar():
        pprint.pprint(agenda)

    if opcion == 'a':
        opcion_add_modificar()
    if opcion == 'b':
        opcion_buscar()
    if opcion == 'c':
        opcion_borrar()
    if opcion == 'd':
        opcion_listar()
    if opcion == 'e':
        break
   
