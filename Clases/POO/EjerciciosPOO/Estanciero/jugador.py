class Jugador():
    def __init__(self,nombre,avatar,dinero,casillero):
        self.__nombre = nombre
        self.__avatar = avatar
        self.__dinero = dinero
        self.__propiedades = []
        self.__casillero = casillero

    #Getters
    def get_nombre(self):
        return self.__nombre
    def get_avatar(self):
        return self.__avatar
    def get_dinero(self):
        return self.__dinero
    def get_casillero(self):
        return self.__casillero
    
    #Setters
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_avatar(self,avatar):
        self.__avatar = avatar
    def set_dineroAdd(self,dinero):
        self.__dinero = dinero
    def set_dineroRestar(self,dinero):
        self.__dinero = dinero
  
    #Metodos 
    def pagarAlquiler(self,propiedad):
        if propiedad.get_propietario() != self and propiedad.get_propietario() != None:
            if propiedad.get_alquiler() <= self.get_dinero():
                propiedad.cobrarAlquiler(self)
            else:
                print("No tenes dinero")
        elif propiedad.get_propietario() == None:
            print("La propiedad no tiene dueño, puedes comprarla")
        else:
            print("Tú eres el dueño de la propiedad,sigue adelante!")
    
    def comprarPropiedad(self,propiedad):
      if propiedad.get_precio() <= self.get_dinero():
        self.__dinero -= propiedad.get_precio()
        self.__propiedades.append(propiedad)
        propiedad.set_propietario(self)
      else:
        print("No tiene suficiente dinero para realizar la compra")
      
    def mostrarPropiedades(self):
      for i in range(len(self.__propiedades)):
        print(f"Propiedad: {self.__propiedades[i].get_nombre()}")
    
    def eliminarPropiedad(self,nombrePropiedad):
      #print(nombrePropiedad.get_nombre())
      self.__indice = self.__propiedades.index(nombrePropiedad)
      #print(self.__indice)
      del self.__propiedades[self.__indice]
      #print(nombrePropiedad.get_nombre())

    def dineroAdd(self,dinero):
        self.__dinero += dinero
    def dineroRestar(self,dinero):
        self.__dinero -= dinero