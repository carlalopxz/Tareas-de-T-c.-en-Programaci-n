from validate_email import validate_email

class Validador():
    def __init__(self):
        pass

    def validarFormulario(self,formulario):
        for key in formulario.keys():
            if key == "email":
                self.validarEmail(self,key,formulario)
            else:
                self.validarCampo(self,key,formulario)
    
    def validarCampo(self,campo,formulario):
        if formulario[campo] == None or formulario[campo] == "":
            print(f"¡Error! falto completar el '{campo}'")
            formulario[campo] = input(f"Complete el {campo}:  ")
            self.validarCampo(self,campo,formulario)

    def validarEmail(self,campo,formulario):
        if formulario[campo] == None or formulario[campo] == "":
            print(f"¡Error! falto completar el '{campo}'")
            formulario[campo] = input(f"Complete el {campo}:  ")
            self.validarCampo(self,campo,formulario)
        elif validate_email(formulario[campo], verify=True) == False:
            print("¡Error! su e-mail no tiene formato de e-mail")
            formulario[campo] = input(f"Complete el {campo} (usuario@correo.com):  ")
            self.validarCampo(self,campo,formulario)

    def validarPosteo(self):
        pass


