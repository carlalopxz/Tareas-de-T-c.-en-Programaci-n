import mysql.connector

configuracion = {
    "host":"localhost",
    "user": "root",
    "password": "",
    "database": "redsocial"
}

class DB():
    def __init__(self):
        self.__conexion = mysql.connector.connect(**configuracion)
        self.__cursor = self.__conexion.cursor()

    
    def get_conexion(self):
        return self.__conexion
    def get_cursor(self):
        return self.__cursor

    def selectNombreCiudad(self):
        sql = 'SELECT nombre FROM ciudad'
        baseDatos.get_cursor().execute(sql)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado
    
    def selectIDCiudad(self,nombreCiudad):
        sql = 'SELECT id FROM ciudad WHERE nombre = %s'
        val = (nombreCiudad,)
        baseDatos.get_cursor().execute(sql,val)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado

    def selectNombreSentimental(self):
        sql = 'SELECT nombre FROM sentimental'
        baseDatos.get_cursor().execute(sql)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado

baseDatos = DB()