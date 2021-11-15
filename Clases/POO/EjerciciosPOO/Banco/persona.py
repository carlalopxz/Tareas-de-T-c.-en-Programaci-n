from cliente import Cliente 

class Persona(Cliente):
    def __init__(self, nombre, apellido, documento, email, password):
        super().__init__(nombre, apellido, documento, email, password)

class PYME(Cliente):
    def __init__(self, nombre, apellido, documento, email, password,CUIT,razonSocial):
        super().__init__(nombre, apellido, documento, email, password)
    
        self.__CUIT = CUIT 
        self.__razonSocial = razonSocial
    
    def get_CUIT(self):
        return self.__CUIT
    def get_razonSocial(self):
        return self.__razonSocial

    def set_CUIT(self,CUIT):
        self.__CUIT = CUIT
    def set_razonSocial(self,razonSocial):
        self.__razonSocial = razonSocial

class Multinacional(Cliente):
    def __init__(self, nombre, apellido, documento, email, password,CUIT,razonSocial):
        super().__init__(nombre, apellido, documento, email, password)

        self.__CUIT = CUIT 
        self.__razonSocial = razonSocial
    
    def get_CUIT(self):
        return self.__CUIT
    def get_razonSocial(self):
        return self.__razonSocial

    def set_CUIT(self,CUIT):
        self.__CUIT = CUIT
    def set_razonSocial(self,razonSocial):
        self.__razonSocial = razonSocial
