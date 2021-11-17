from baseDeDatos import baseDatos
class Ciudad():
    def __init__(self):
        pass
    
    def get_ciudadID(self):
        return self.__ciudadID

    def set_ciudadID(self, id):
        self.__ciudadID = id

    def selectIDCiudad(self,nombreCiudad):
        sql = 'SELECT id FROM ciudad WHERE nombre = %s'
        val = (nombreCiudad,)
        baseDatos.get_cursor().execute(sql,val)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado

ciudadInstancia = Ciudad()

