from random import randint
from propiedad import Propiedad
from jugador import Jugador
from estanciero import Estanciero

propiedad1 = Propiedad("Corrientes",100,20,1)
propiedad2 = Propiedad("Avellaneda",150,10,2)
propiedad3 = Propiedad("Castelar",200,50,3)
propiedad4 = Propiedad("Parque Chas",500,50,4)
propiedad5 = Propiedad("Villa Urquiza",300,50,5)
propiedad6 = Propiedad("Belgrano",200,30,6)

jugador1 = Jugador("Lucas",None,1000,None)
jugador2 = Jugador("Carla",None,1000,None)
jugador3 = Jugador("Carina",None,1000,None)
#None
print(f"Propietario de {propiedad1.get_nombre()}: {propiedad1.get_propietario()}")
#Dinero inicial
print(f"Dinero disponible de {jugador1.get_nombre()}: {jugador1.get_dinero()}")
# Compro la propiedad que paso como parametro y si el valor es menor +
# o igual al dinero que tengo disponible, me descuenta ese dinero 
# y agrega la propiedad a la lista de propiedades
jugador1.comprarPropiedad(propiedad1)
#Jugador
print(f"Propietario de {propiedad1.get_nombre()}: {propiedad1.get_propietario().get_nombre()}")
#Dinero final
print(f"Dinero disponible de {jugador1.get_nombre()} :{jugador1.get_dinero()}")

jugador1.comprarPropiedad(propiedad2)
print(jugador1.mostrarPropiedades())
jugador1.eliminarPropiedad(propiedad2)

estanciero = Estanciero(None,None,None)
estanciero.agregarJugadores(jugador1)
estanciero.agregarJugadores(jugador2)
estanciero.agregarJugadores(jugador3)
print("LISTA JUGADORES")
estanciero.mostrarJugadores()
#estanciero.eliminarJugadores(jugador1)
#estanciero.mostrarJugadores()
print("JUGADOR ACTIVO")
print(estanciero.get_jugadorActivo(randint(0,3)).get_nombre())
print(estanciero.tirarDados())
print(jugador1.get_dinero())
print(jugador2.get_dinero())
propiedad2.cobrarAlquiler(jugador2)
print(jugador2.get_dinero())
print(jugador1.get_dinero())
