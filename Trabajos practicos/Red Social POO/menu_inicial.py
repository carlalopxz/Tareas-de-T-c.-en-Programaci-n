# from datetime import datetime
from ciudad import ciudadInstancia

class MenuInicial():
    def __init__(self):
        pass

    def menu(self):
        opcion = False
        while opcion == False:  
            option = input("Seleccione la accion a realizar:\nA) Registrar usuario\nB) Loguearse\nOpción:").lower()
            if option == "a":
                self.registrarUsuario()
                opcion = True
            elif option == "b":
                pass
                opcion = True

    def registrarUsuario(self):
        formulario = {
            "nombre":None,
            "apellido":None,
            "email":None,
            "password":None,
            "sexo":None,
            "imagenPerfil":None,
            "imagenPortada":None,
            "biografia":None,
            "celular":None,
            "fechaCreacionCuenta":None,
            "ciudad":None,
            "sentimental":None
        }
        # formulario["nombre"] = input("Ingrese el nombre del usuario:  ").capitalize()
        # formulario["apellido"] = input("Ingrese el nombre del apellido:  ").capitalize()
        # formulario["email"] = input("Ingrese el mail del usuario:  ").lower()
        # formulario["password"] = input("Ingrese la contraseña del usuario:  ").lower()
        # formulario["sexo"] = input("Ingrese el sexo del usuario (H - M):  ").upper()
        # formulario["imagenPerfil"] = input("Ingrese la foto de perfil (URL): ").lower()
        # formulario["imagenPortada"] = input("Ingrese la imagen de portada (URL):  ").lower()
        # formulario["biografia"] = input("Ingrese la biografia:  ").capitalize()
        # formulario["celular"] = input("Ingrese el celular del usuario:  ")
        # formulario["fechaCreacionCuenta"] = (f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")
        ciudadInput = input("Ingrese el nombre de la ciudad:  ").capitalize()
        for x in ciudadInstancia.selectIDCiudad(ciudadInput):
            for y in x:
                ciudadInstancia.set_ciudadID(y)
                formulario["ciudad"] = ciudadInstancia.get_ciudadID()
        print(formulario)


menu = MenuInicial()

menu.menu()