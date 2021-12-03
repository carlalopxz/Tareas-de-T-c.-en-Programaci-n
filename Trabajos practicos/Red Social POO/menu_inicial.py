from datetime import datetime
from baseDeDatos import baseDatos
from menu_usuario import MenuUsuario
from validador import Validador
import stdiomask,time
from validador_logueo import ValidadorLoguin

class MenuInicial():
    def __init__(self):
        pass

    def menu(self):
        opcion = False
        while opcion == False:  
            option = input("\n\nSeleccione la accion a realizar:\nA) Registrar usuario\nB) Loguearse\nOpción: ").lower()
            if option == "a":
                self.registrarUsuario()
                opcion = True
            elif option == "b":
                self.loguearUsuario()
                opcion = True

    def registrarUsuario(self):
        formulario = {
            "nombre":None,
            "apellido":None,
            "email":None,
            "celular":None,
            "password":None,
            "cpassword":None,
            "sexo":None,
            "imagenPerfil":None,
            "imagenPortada":None,
            "biografia":None,
            "fechaCreacionCuenta":None,
            "sentimental":None,
            "ciudad":None
        }

        formulario["nombre"] = (input("Ingrese el nombre del usuario:  ").capitalize()).strip()
        formulario["apellido"] = (input("Ingrese el nombre del apellido:  ").capitalize()).strip()
        formulario["email"] = (input("Ingrese el mail del usuario:  ").lower()).strip()
        formulario["celular"] = (input("Ingrese el celular del usuario:  ")).strip()
        formulario["password"] = (stdiomask.getpass(prompt="Ingrese su password que contenga al menos una minuscula, una mayuscula y alguno de los siguientes caracteres especiales '$ % # @': \n", mask = "*")).strip()
        formulario["cpassword"] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*"))
        formulario["sexo"] = (input("Ingrese el sexo del usuario (H - M):  ").upper()).strip()
        formulario["imagenPerfil"] = (input("Ingrese la foto de perfil (URL): ").lower()).strip()
        formulario["imagenPortada"] = (input("Ingrese la imagen de portada (URL):  ").lower()).strip()
        formulario["biografia"] = (input("Ingrese la biografia (NULL para agregar despues):  ").capitalize()).strip()
        formulario["fechaCreacionCuenta"] = (f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")
        
        print("Situacion sentimental:")
        cont = 1
        for x in baseDatos.selectNombreSentimental():
            for y in x:
                print(f"\t• {cont}: {y}")
            cont += 1
        formulario["sentimental"] = int(input("Ingrese su situacion sentimental:  "))
        print("Ciudad")
        cont = 1
        for x in baseDatos.selectNombreCiudad():
            for y in x:
                print(f"\t• {cont}: {y}")
            cont += 1
        formulario["ciudad"] = int(input("Ingrese el nombre de la ciudad:  "))

        Validador.validarFormulario(Validador,formulario)
        time.sleep(5) #Espera 10 segundos antes de loguearse 
        MenuInicial.loguearUsuario()
        return formulario

    def loguearUsuario(self):
        formulario = { }
        while True:
            opcion = input('\n\nA) Ingresar con email\nB) Ingresar con celular\nC) Ingresar despues\nOpcion:  ').lower()
            if opcion == 'a':
                formulario['email'] = (input('Ingrese su mail: ')).strip()
            elif opcion == 'b':
                formulario['celular'] = (input('Ingrese su celular: ')).strip()
            elif opcion == 'c':
                print('Hasta Pronto')
                break
            else:
                print('Opcion incorrecta, vuelva a intentar.')
            formulario['password'] = (stdiomask.getpass(prompt='Ingrese su contraseña: ',mask='*')).strip()
            break       
        resultado = ValidadorLoguin.validarLogueo(ValidadorLoguin,formulario)
        time.sleep(5)
        if resultado == True:
            if opcion == 'a':
                nombre = baseDatos.selectNombreConEmail(formulario['email'])[0][0]
                print(f'Hola! {nombre}')
            if opcion == 'b':
                nombre = baseDatos.selectNombreConCelular(formulario['celular'])[0][0]
                print(f'Hola! {nombre}')
        time.sleep(5)
        MenuUsuario