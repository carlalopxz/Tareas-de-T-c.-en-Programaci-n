from datetime import datetime
from baseDeDatos import baseDatos
from validador import Validador


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
            "cpassword":None,
            "sexo":None,
            "imagenPerfil":None,
            "imagenPortada":None,
            "biografia":None,
            "celular":None,
            "fechaCreacionCuenta":None,
            "ciudad":None,
            "sentimental":None
        }

        formulario["nombre"] = input("Ingrese el nombre del usuario:  ").capitalize()
        formulario["apellido"] = input("Ingrese el nombre del apellido:  ").capitalize()
        formulario["email"] = input("Ingrese el mail del usuario:  ").lower()
        formulario["password"] = input("Ingrese su password que contenga al menos una minuscula, una mayuscula y alguno de los siguientes caracteres especiales '$ % # @' ")
        formulario["cpassword"] = input("Ingrese nuevamente la contraseña del usuario:  ")
        formulario["sexo"] = input("Ingrese el sexo del usuario (H - M):  ").upper()
        formulario["imagenPerfil"] = input("Ingrese la foto de perfil (URL): ").lower()
        formulario["imagenPortada"] = input("Ingrese la imagen de portada (URL):  ").lower()
        formulario["biografia"] = input("Ingrese la biografia:  ").capitalize()
        formulario["celular"] = input("Ingrese el celular del usuario:  ")
        formulario["fechaCreacionCuenta"] = (f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")
        
        print("Ciudad")
        cont = 1
        for x in baseDatos.selectNombreCiudad():
            for y in x:
                print(f"\t• {cont}: {y}")
            cont += 1
        ciudadInput = int(input("Ingrese el número de su ciudad: "))
        formulario["ciudad"] = ciudadInput

        print("Situacion sentimental:")
        cont = 1
        for x in baseDatos.selectNombreSentimental():
            for y in x:
                print(f"\t• {cont}: {y}")
            cont += 1
        sentimentalInput = int(input("Ingrese el numero de su situacion sentimental:  "))
        formulario["sentimental"] = sentimentalInput
        
        Validador.validarFormulario(Validador,formulario)
                


menu = MenuInicial()

menu.menu()