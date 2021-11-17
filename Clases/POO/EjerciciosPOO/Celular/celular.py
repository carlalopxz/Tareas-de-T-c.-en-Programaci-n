from base import db

class Celular():
    def __init__(self,marca,modelo,proveedorDeLinea,numero):
        self.__marca = marca
        self.__modelo = modelo
        self.__proveedorDeLinea = proveedorDeLinea
        self.__numero = numero
        self.__id = 0
    
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_proveedor(self):
        return self.__proveedorDeLinea
    def get_numero(self):
        return self.__numero
    def get_id(self):
        return self.__id
    
    def set_marca(self,marca):
        self.__marca= marca
    def set_modelo(self,modelo):
        self.__modelo = modelo
    def set_proveedor(self,proveedor):
        self.__proveedorDeLinea = proveedor
    def set_numero(self,numero):
        self.__numero = numero
    def set_id(self, ids):
        self.__id = ids 
    
    def save(self):
        sql = 'INSERT INTO celular (marca,modelo,proveedor,numero) VALUES (%s,%s,%s,%s)'
        val = (self.get_marca(),self.get_modelo(),self.get_proveedor(),self.get_numero())
        db.get_cursor().execute(sql,val)
        db.get_conexion().commit()

        self.set_id(db.get_cursor().lastrowid)
    
    def delete(self,id):
        sql = 'DELETE FROM celular WHERE celularID = %s'
        val = (id,)
        db.get_cursor().execute(sql,val)
        db.get_conexion().commit()

    def select(self):
        sql = "SELECT celularID from celular WHERE modelo = %s"
        val = (self.get_modelo(),)
        db.get_cursor().execute(sql,val)
        resultado = db.get_cursor().fetchall()
        return resultado

    
celular1 =  Celular("Motorola","Moto G30","Claro","1139080645")
celular2 =  Celular("Motorola","Moto G20","Claro","1139080645")

# celular1.save()
# celular2.save() #me guarda en ID 4 ??¿¿

resultado = celular1.select()

for x in resultado:
    for i in x:
        celular1.delete(i)

# print(celular2.get_id())

# celular2.delete()