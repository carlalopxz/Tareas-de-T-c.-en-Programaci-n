import base64
import stdiomask
from baseDeDatos import baseDatos
from validador import Validador
from validador_logueo import ValidadorLoguin

class Usuario():
    def __init__(self,nombre, apellido,email, celular,password, cpassword,sexo, imagenPerfil,
    imagenPortada,biografia,fechaCreacionCuenta,sentimental,ciudad):
        self.__id = baseDatos.selectIDUsuario() + 1
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__celular = celular
        self.__password = password
        self.__cpassword = cpassword
        self.__sexo = sexo
        self.__imagenPerfil = imagenPerfil
        self.__imagenPortada = imagenPortada
        self.__biografia = biografia
        self.__fechaCreacionCuenta = fechaCreacionCuenta
        self.__sentimental = sentimental
        self.__ciudad = ciudad
    
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password 
    def get_sexo(self):
        return self.__sexo
    def get_imagenPerfil(self):
        return self.__imagenPerfil
    def get_imagenPortada(self):
        return self.__imagenPortada
    def get_biografia(self):
        return self.__biografia
    def get_celular(self):
        return self.__celular
    def get_fechaCreacionCuenta(self):
        return self.__fechaCreacionCuenta
    def get_ciudad(self):
        return self.__ciudad
    def get_sentimental(self):
        return self.__sentimental
    def get_cpassword(self):
        return self.__cpassword
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_email(self,email):
        self.__email = email
    def set_password(self,password):
        self.__password = password
    def set_sexo(self,sexo):
        self.__sexo = sexo
    def set_imagenPerfil(self,imagenPerfil):
        self.__imagenPerfil = imagenPerfil
    def set_imagenPortada(self,imagenPortada):
        self.__imagenPortada = imagenPortada
    def set_biografia(self,biografia):
        self.__biografia = biografia
    def set_celular(self,celular):
        self.__celular = celular
    def set_fechaCreacionCuenta(self,fechaNueva):
        self.__fechaCreacionCuenta = fechaNueva
    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad
    def set_sentimental(self,sentimental):
        self.__sentimental = sentimental

    def menuUsuarioInicial(self):
        print('\nMENU USUARIO')
        while True:
            opcion = (input('''\nSeleccione una opcion:
            A) Modificar usuario
            B) Dar de baja
            C) Agregar amigo
            D) Eliminar amigo
            E) Listado de amigos
            F) SALIR!
            Opcion:  ''').lower()).strip()
            if opcion == 'a':
                self.menuUsuarioModificar(opcion)
            if opcion == 'f':
                print('Hasta pronto!')
                break
    
    def menuUsuarioModificar(self,opcion):
        while True:
            opcion = (input('''\nSeleccione una opcion a modificar:
            A) Nombre
            B) Apellido
            C) Email
            D) Celular
            E) Contraseña
            F) Sexo
            G) Imagen de Perfil
            H) Imagen de Portada
            I) Biografía
            J) Situación sentimental
            K) Ciudad
            M) SALIR!
            Opcion:  ''').lower()).strip()

            if opcion == 'a':
                self.modificarNombre()
            elif opcion == 'b':
                self.modificarApellido()
            elif opcion == 'c':
                self.modificarEmail()
            elif opcion == 'd':
                self.modificarCelular()
            elif opcion == 'e':
                self.modificarPassword()
            elif opcion == 'f':
                self.modificarSexo()
            elif opcion == 'g':
                pass
            elif opcion == 'h':
                pass
            elif opcion == 'i':
                pass
            elif opcion == 'j':
                pass
            elif opcion == 'k':
                pass
            elif opcion == 'm':
                print('\n\nHasta pronto!')
                break
            else:
                print('Opcion equivocada, intenta nuevamente!')
    
    def modificarNombre(self):
        formularioMod = {}
        while True:
            formularioMod['nombre'] = (input('Ingrese su nombre nuevo:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputNombre = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('nombre',f"'{inputNombre}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
                    
    def modificarApellido(self):
        formularioMod = {}
        while True:
            formularioMod['apellido'] = (input('Ingrese su apellido nuevo:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputApellido = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('apellido',f"'{inputApellido}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
                    
    def modificarEmail(self):
        formularioMod = {}
        while True:
            formularioMod['email'] = (input('Ingrese su mail nuevo:  ')).strip()
            formularioMod['celular'] = (input('Ingrese su celular:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            formularioMod2 = {
                'celular': formularioMod['celular'],
                'password': formularioMod['password']}
            inputEmail = Validador.validarEmail(Validador,'email',formularioMod) #chico@gmail.com
            inputCelular = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod2)[-1]
            if inputCelular == self.get_celular():
                print(baseDatos.modificacionUsuario('email',f"'{inputEmail}'",'celular',f"'{inputCelular}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         

    def modificarCelular(self):
        formularioMod = {}
        while True:
            formularioMod['celular'] = (input('Ingrese su celular nuevo:  ')).strip()
            formularioMod['email'] = (input('Ingrese su mail:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            formularioMod2 = {
                'email': formularioMod['email'],
                'password': formularioMod['password']}
            inputCelular = Validador.validarCelular(Validador,'celular',formularioMod) 
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod2)[-1]
            if inputEmail == self.get_email():
                print(baseDatos.modificacionUsuario('celular',f"'{inputCelular}'",'email',f"'{inputEmail}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
    
    def modificarPassword(self):
        while True:
            formulario = {}
            formularioMod = {}
            formulario['password'] = 'Chico99@'#(stdiomask.getpass(prompt='Ingrese su actual password:  ',mask='*')).strip()
            formularioMod['password'] = 'Chiquito99@'#(stdiomask.getpass(prompt='Ingrese su nueva password:  ',mask='*')).strip()
            formularioMod['cpassword'] = 'Chiquito99@'#(stdiomask.getpass(prompt='Ingrese nuevamente su password:  ',mask='*')).strip()
            formulario['email'] = 'chiquito@gmail.com' #(input('Ingrese su correo electronico:  ')).strip()
            validacionPassVieja = ValidadorLoguin.validarPassword(ValidadorLoguin,formulario)
            password = base64.b64decode(self.get_password().encode('UTF-8')).decode('UTF-8')
            if formulario['email'] == self.get_email():
                if validacionPassVieja == password:
                    validarPassNueva = Validador.validarPassword(Validador,'password',formularioMod)
                    print(baseDatos.modificarUsuarioPass('contrasenia','ccontrasenia',f"'{validarPassNueva[0]}'",'email',f"'{formulario['email']}'"))
                    break
            else:
                print('Estas tratando de modificar un usuario que no te pertenece!')

    def modificarSexo(self):
        while True:
            formularioMod = {}
            while True:
                opcion= (input('\nSeleecione su nuevo sexo:\nA) Hombre\nB) Mujer\nOpcion:  ').lower()).strip()
                if opcion == 'a':
                    formularioMod['sexo'] = 'H'
                    break
                elif opcion == 'b':
                    formularioMod['sexo'] = 'M'
                    break
                else:
                    print('\nOpcion incorrecta! ')
            formularioMod['email'] = (input('Ingrese su email:  ')).strip()
            formularioMod['password'] =  (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputSexo = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('sexo',f"'{inputSexo}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')    
            

    def bajaUsuario(self):
        pass

    def agregarAmigo(self):
        pass

    def eliminarAmigo(self):
        pass

    def listadoAmigos():
        pass


