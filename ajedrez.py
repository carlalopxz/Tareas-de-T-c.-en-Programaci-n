#  a) Un tablero de ajedrez debe tener en cada equipo (blancas y negras): 

#  Entre 0 y 8 Peones
#  Entre 0 y 2 Caballos
#  Entre 0 y 2 Alfiles
#  Entre 0 y 2 Torres
#  Entre 0 y 1 Reina
#  1 Rey
import random 
#Creación del tablero 
tablero = ['__'] * 8
for i in range(8):
    tablero[i] = ['__'] * 8
# Posicionamiento de piezas 
piezas = ['pB','tB','cB','aB','rB','dB','pN','tN','cN','aN','rN','dN']
for blancas in piezas:
    pB = random.randint(0,8)
    tB = random.randint(0,2)
    cB = random.randint(0,2)
    aB = random.randint(0,2)
    rB = random.randint(0,1)
    dB = random.randint(0,1)
    
for x in tablero:
    print(x)     



