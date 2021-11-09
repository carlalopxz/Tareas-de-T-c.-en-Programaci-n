import base64, mysql.connector

class Usuario():
    def __init__(self,nombre,mail,contrasenia,celular,id):
        self.__nombre = nombre
        self.__mail =mail
        #self.__contrasenia = contrasenia
        self.set_contrasenia(contrasenia)
        self.__celular = celular
        self.__habilidades = []
        self.__id = id
    
    def get_nombre(self):
        return self.__nombre
    def get_mail(self):
        return self.__mail
    def get_contrasenia(self):
        return self.__contrasenia
    def get_celular(self):
        return self.__celular
    def get_id(self):
        return self.__id
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_mail(self,mail):
        self.__mail = mail
    def set_contrasenia(self,contrasenia):
        self.__contrasenia = self._encriptarContrasenia(contrasenia)
    def set_celular(self,celular):
        self.__celular = celular
    def set_id(self,id):
        self.__id = id
    
    def saludar(self):
        print(f"Hola {self.__nombre}")
    
    #def encriptarContrasenia(self):
    #    a = self.__contrasenia.encode("UTF-8")
    #    b = base64.b64encode(a)
    #    c = b.decode("UTF-8")
    #    print(f"Constraseña Encriptada: {c}")
    #    d = c.encode("UTF-8")
    #    e = base64.b64decode(d)
    #    f = e.decode("UTF-8")
    #    print(f"Contraseña: {f}")

    def _encriptarContrasenia(self,contrasenia):
      return base64.b64encode(contrasenia.encode("UTF-8")).decode("UTF-8")
    
    def mostrarTelefono(self):
        print(f"Marca: {self.__celular.get_marca()}\nModelo: {self.__celular.get_modelo()}\nProveedor de linea: {self.__celular.get_proveedor()}\nNumero: {self.__celular.get_numero()}\nY son fan de los {self.__celular.get_marca()}")

    def llamar(self,usuario,duracionLlamadaXMin):
      if self.__celular.get_proveedor() == usuario.get_celular().get_proveedor():
        print("La llamada es gratis")
      else:
        costoLlamada = duracionLlamadaXMin * 10
        print(f"El costo de la llamada es de: ${costoLlamada} pesos")

    def agregarHabilidad(self,habilidad):
        self.__habilidades.append(habilidad)
    
    def eliminarHabilidad(self,habilidad):
        self.__habilidades.remove(habilidad)
    
    def saberHacer(self,string,puntaje):
        #[objeto1,objeto2] = i en la primera vuelta = objeto1
        resultado = []
        for i in self.__habilidades:
                        #objeto1 
            if string == i.get_nombre() and puntaje <= i.get_expertise():
                resultado.append(True)
            else:
                resultado.append(False)
        print(resultado)
    
    def guardar(self,usuario):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="python")
        baseDeDatos = mydb.cursor()
        sql = "INSERT INTO contactos (id,nombre, email, celular) VALUES (%s, %s,%s,%s)"
        val = (f"{usuario.get_id()}",f"{usuario.get_nombre()}", f"{usuario.get_mail()}",f"{str(usuario.get_celular().get_numero())}")
        baseDeDatos.execute(sql,val)
        mydb.commit()
        print(baseDeDatos.rowcount, "record inserted.")
    
    def eliminar(self,usuario):
        pass