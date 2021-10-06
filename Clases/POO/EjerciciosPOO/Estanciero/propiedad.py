class Propiedad():
    def __init__(self,nombre,precio,alquiler,casillero):
        self.__nombre = nombre
        self.__precio = precio
        self.__alquiler = alquiler
        self.__casillero = casillero
        self.__propietario = None

    #Getters
    def get_nombre(self):
      return self.__nombre
    def get_precio(self):
      return self.__precio
    def get_alquiler(self):
      return self.__alquiler
    def get_casillero(self):
      return self.__casillero
    def get_propietario(self):
      return self.__propietario

    #Setters
    def set_nombre(self,nombre):
      self.__nombre = nombre
    def set_precio(self,precio):
      self.__precio = precio
    def set_alquiler(self,alquiler):
      self.__alquiler = alquiler
    def set_casillero(self,casillero):
      self.__casillero = casillero
    def set_propietario(self,propietario):
      self.__propietario = propietario

    #Metodos
    def cobrarAlquiler(self,jugador):
      jugador.dineroRestar(self.__alquiler)
      self.__propietario.dineroAdd(self.__alquiler)
    