class Personal():
    def __init__(self,nombre,apellido,dni,sueldo,comision):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__sueldo = sueldo
        self.__comision = comision
    #getters
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_dni(self):
        return self.__dni
    def get_sueldo(self):
        return self.__sueldo
    def get_comision(self):
        return self.__comision
    #setters
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_dni(self,dni):
        self.__dni = dni
    def set_sueldo(self,sueldo):
        self.__sueldo = sueldo
    def set_comision(self,comision):
        self.__comision = comision

class empleadoMostrador(Personal):
    def __init__(self, nombre, apellido, dni, sueldo, comision):
        super().__init__(nombre, apellido, dni, sueldo, comision)

    #Metodos
    def cobrar(self,articulo):
        pass
    def sumarDineroCaja(self,articulo):
        pass
    def restarDineroCaja(self):
        pass

class empleadoComun(Personal):
    def __init__(self, nombre, apellido, dni, sueldo, comision):
        super().__init__(nombre, apellido, dni, sueldo, comision)
    #Metodos
    def venderArticulos(self,articulo):
        pass
    def generarComision(self,articulo):
        pass