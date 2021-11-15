from abc import ABC

class Cliente(ABC):
    def __init__(self, nombre, apellido, documento, email, password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento = documento
        self.__email = email
        self.__password = password

    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_documento(self):
        return self.__documento
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_documento(self,documento):
        self.__documento = documento
    def set_email(self,email):
        self.__email = email
    def set_password(self,password):
        self.__password = password
    
    