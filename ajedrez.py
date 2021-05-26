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
# Posicionamiento de piezas blancas
pB = random.randint(0,8)
tB = random.randint(0,2)
cB = random.randint(0,2)
aB = random.randint(0,2)
rB = 1
dB = random.randint(0,1)
piezasBlancas = [pB,tB,cB,aB,rB,dB]
pBlanc = ['pB','tB','cB','aB','rB','dB']
indice_blancas=0
for i in piezasBlancas:
    for j in range(i):
        tablero[random.randint(0,7)][random.randint(0,7)] = pBlanc[indice_blancas]
    indice_blancas += 1
#Posicionamiento de piezas negras 
pN = random.randint(0,8)
tN = random.randint(0,2)
cN = random.randint(0,2)
aN = random.randint(0,2)
rN = 1
dN = random.randint(0,1)
piezasNegras = [pN,tN,cN,aN,rN,dN]
pBlanc = ['pN','tN','cN','aN','rN','dN']
indice_negras=0
for i in piezasBlancas:
    for j in range(i):
        tablero[random.randint(0,7)][random.randint(0,7)] = pBlanc[indice_negras]
    indice_negras += 1
#Impresiòn de tablero
for x in tablero:
    print(x)     



