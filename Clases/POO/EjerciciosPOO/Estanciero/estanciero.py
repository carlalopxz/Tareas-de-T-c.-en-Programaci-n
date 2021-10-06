from random import randint

class Estanciero():
    def __init__(self,propiedades,dineroDisponible,jugadorActivo):
        self.__numeroDado = 0
        self.__propiedades = []
        self.__dineroDisponible = dineroDisponible
        self.__jugadores = []
        self.__jugadorActivo = jugadorActivo
    
    #Getters
    def get_numeroDado(self):
      return self.__numeroDado
    def get_propiedades(self):
      return self.__propiedades.get_nombre()
    def get_dineroDisponible(self):
      return self.__dineroDisponible
    def get_jugadorActivo(self,i):
      self.__jugadorActivo = self.__jugadores[i % len(self.__jugadores)]
      return self.__jugadores[i % len(self.__jugadores)]
    #Setters
    def set_numeroDado(self,numeroDado):
      self.__numeroDado = numeroDado
    def set_dineroDisponible(self,dinero):
      self.__dineroDisponible = dinero

    #Metodos
    def tirarDados(self):
      for i in range(2):
        self.__numeroDado+= randint(1,6)
      return f"Te mueves {self.__numeroDado} lugares"
    

    def agregarJugadores(self,jugador):
      self.__jugadores.append(jugador)
    
    def eliminarJugadores(self,jugador):
      self.__jugadores.remove(jugador)

    def mostrarJugadores(self):
      for i in self.__jugadores:
        print(i.get_nombre())
      
    def agregarPropiedades(self,propiedad):
      self.__propiedades.append(propiedad)
    
    def eliminarPropiedades(self,propiedad):
      self.__propiedades.remove(propiedad)
