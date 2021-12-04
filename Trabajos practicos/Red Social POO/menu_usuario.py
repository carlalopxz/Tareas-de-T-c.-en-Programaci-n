from main import usuario

class MenuUsuario():
    def __init__(self):
        pass

    def menuUsuario(self):
        print('\nMENU USUARIO')
        while True:
            opcion = input('\nSeleccione una opcion:\nA) Modificar usuario\nB) Dar de baja\nC) Agregar amigo\nD) Eliminar amigo\nE) Listado de amigos\nOpcion:  ').lower()
            if opcion == 'a':
                while True:
                    opcionA = input('''\nSeleccione una opcion a modificar:
A) Nombre
B) Apellido
''')



menu = MenuUsuario()
menu.menuUsuario()