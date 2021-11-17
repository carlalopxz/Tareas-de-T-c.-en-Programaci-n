import mysql.connector

configuracion = {
    "host":"localhost",
    "user": "root",
    "password": "",
    "database": "usuarios"
}

class BD():
    def __init__(self):
        self.__conexion = mysql.connector.connect(**configuracion)
        self.__cursor = self.__conexion.cursor()

    
    def get_conexion(self):
        return self.__conexion
    def get_cursor(self):
        return self.__cursor

    def insertarRegistro():
        pass

db = BD();