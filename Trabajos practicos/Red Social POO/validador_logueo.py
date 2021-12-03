from baseDeDatos import baseDatos
import base64

class ValidadorLoguin():
    def __init__(self):
        pass

    def validarLogueo(self,formulario):
        for key in formulario.keys():
            if key == "email":
                email = self.validarEmail(self,key,formulario)
                password = self.validarPassword(self,formulario)
            elif key == "celular":
                celular = self.validarCelular(self,key,formulario)
                password = self.validarPassword(self,formulario)          
        if email and password == True or celular and password == True:
            return True
    
    def validarEmail(self,key,formulario):
        if formulario[key] == '' or formulario[key] == None:
            print('Debe llenar el campo EMAIL!')
            formulario[key] = (input("Intente de nuevo con su correo:  ")).strip()
            self.validarEmail(self,key,formulario)
        else:
            if baseDatos.selectEmail(key,formulario) == []:
                print('Este correo no existe en nuestra base de datos.')
                formulario[key] = (input("Intente de nuevo con su correo:  ")).strip()
                self.validarEmail(self,key,formulario)
        return True

    def validarPassword(self,formulario):
        keys = list(formulario.keys())
        if keys[0] == 'email':
            password = base64.b64decode(baseDatos.selectNombreConEmail(formulario['email'])[0][-1].encode('UTF-8')).decode('UTF-8')
        elif keys[0] == 'celular':
            password = base64.b64decode(baseDatos.selectNombreConCelular(formulario['celular'])[0][-1].encode('UTF-8')).decode('UTF-8')
        #     password = base64.b64decode(baseDatos.selectNombreConEmail(formulario['email'])[0][-1].encode('UTF-8')).decode('UTF-8')
        if password != formulario['password'] or formulario['password'] == '' or formulario['password'] == None:
            print('Contraseña incorrecta, intente nuevamente')
            formulario['password'] = (input('Ingrese su password:  ')).strip()
            self.validarPassword(self,formulario)
        return True
        
    
    def validarCelular(self,key,formulario):
        if formulario[key] == '' or formulario[key] == None:
            print('Debe llenar el campo CELULAR!')
            formulario[key] = (input("Ingrese su celular nuevamente:  ")).strip()
            self.validarCelular(self,key,formulario)
        if baseDatos.selectCelular(key,formulario) == []:
            print('Este celular no se encuentra en nuestra base de datos')
            formulario[key] = (input('Ingrese nuevamente su celular: ')).strip()
            self.validarCelular(self,key,formulario)
        return True
            

