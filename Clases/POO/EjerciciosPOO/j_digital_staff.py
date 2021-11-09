from abc import ABC,abstractmethod

class Persona(ABC):
    def __init__(self,nombre,apellido,email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
    
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_email(self):
        return self.__email
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_email(self,email):
        self.__email = email

    @abstractmethod
    def ingresarAlEdificio(self,ingreso):
        pass

class Empleado(Persona):
    def __init__(self, nombre, apellido, email,sueldo):
        super().__init__(nombre, apellido, email)
        self.__sueldo = sueldo
    
    def get_sueldo(self):
        return self.__sueldo
    
    def set_sueldo(self,sueldo):
        self.__sueldo = sueldo

    def ingresarAlEdificio(self, ingreso):
        print("Ingreso con huella digital")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, email,egresado=False):
        super().__init__(nombre, apellido, email)
        self.__egresado = egresado

    def get_egresado(self):
        return self.__egresado

    def terminarCursada(self):
        self.__egresado = True
    def ingresarAlEdificio(self, ingreso):
        print("Ingreso con tarjeta")

persona_uno = Empleado("Lucas","Croci","email@email.com",30000)
persona_dos = Estudiante("Carla","Lopez","email@email.com")

print(persona_dos.get_egresado())
persona_dos.terminarCursada()
print(persona_dos.get_egresado())