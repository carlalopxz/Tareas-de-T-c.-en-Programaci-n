#  a) Un tablero de ajedrez debe tener en cada equipo (blancas y negras): 

#  Entre 0 y 8 Peones
#  Entre 0 y 2 Caballos
#  Entre 0 y 2 Alfiles
#  Entre 0 y 2 Torres
#  Entre 0 y 1 Reina
#  1 Rey

#b) El programa debe poder calcular el puntaje de cada jugador dependiendo 
# de qué piezas poseen en el tablero: 

#Peones valen 1 punto
#Caballos valen 3 puntos 
#Alfiles valen 3 puntos 
#Torres valen 5 puntos 
#Reinas valen 9 puntos 
#Reyes valen 4 puntos

import random 
#Creación del tablero 
tablero = ['__'] * 8
for i in range(8):
    tablero[i] = ['__'] * 8

puntajes = {'pB':1,'cB':3,'aB':3,'tB':5,'dB':9,'rB':4,'pN':1,'cN':3,'aN':3,'tN':5,'dN':9,'rN':4}

pB = random.randint(0,8)
tB = random.randint(0,2)
cB = random.randint(0,2)
aB = random.randint(0,2)
dB = random.randint(0,1)
rB = 1

pN = random.randint(0,8)
tN = random.randint(0,2)
cN = random.randint(0,2)
aN = random.randint(0,2)
dN = random.randint(0,1)
rN = 1
piezasNegras = [pN,tN,cN,aN,rN,dN]
pNegras = ['pN','tN','cN','aN','rN','dN']
piezasBlancas = [pB,tB,cB,aB,rB,dB]
pBlanc = ['pB','tB','cB','aB','rB','dB']
puntaje_blanca = 0
puntaje_negra = 0
indice_blancas=0
for b in piezasBlancas:
    for j in range(b):
        while True:
            x = random.randint(0,7)
            y = random.randint(0,7)
            if tablero[x][y] == '__':
                tablero[x][y] = pBlanc[indice_blancas]
                puntaje_blanca = puntaje_blanca + puntajes[pBlanc[indice_blancas]]
                break 
    indice_blancas += 1

indice_negras=0
for c in piezasNegras:
    for j in range(c):
        while True:
            x = random.randint(0,7)
            y = random.randint(0,7)
            if tablero[x][y] == '__':
                tablero[x][y] = pNegras[indice_negras]
                puntaje_negra = puntaje_negra + puntajes[pNegras[indice_negras]]
                break
    indice_negras += 1
#Impresiòn de tablero
for x in tablero:
    print(x)     
#Puntajes
print(f'Puntaje de jugador con piezas blancas: {puntaje_blanca}')
print(f'Puntaje de jugador con piezas negras: {puntaje_negra}')
#Jaque
indiceDeLaLista = 0
indiceDentroDeLista = 0
for i in range(len(tablero)):
    if 'rB' in tablero[i]:
        indiceDentroDeLista_blanca = tablero[i].index('rB')
        print('El indice del rey blanco es: ', indiceDentroDeLista_blanca)
        indiceDeLaLista_blanca = tablero.index(tablero[i])
        print('El indice de la lista donde está el rey es:',indiceDeLaLista_blanca)
    if 'rN' in tablero[i]:
        indiceDentroDeLista_negra = tablero[i].index('rN')
        print('El indice del rey negro es: ', indiceDentroDeLista_negra)
        indiceDeLaLista_negra = tablero.index(tablero[i])
        print('El indice de la lista donde está el rey es:',indiceDeLaLista_negra)
fichasNegras = 0
fichasBlancas = 0
jaqueBlanca = tablero[indiceDeLaLista_blanca-1:indiceDeLaLista_blanca+2]
for i in jaqueBlanca:
    for j in i[indiceDentroDeLista_blanca-1:indiceDentroDeLista_blanca+2]:
        if j in pNegras:
            fichasNegras += 1
jaqueNegra = tablero[indiceDeLaLista_negra-1:indiceDeLaLista_negra+2]
for i in jaqueNegra:
    for j in i[indiceDentroDeLista_negra-1:indiceDentroDeLista_negra+2]:
        if j in pBlanc:
            fichasBlancas += 1

if fichasBlancas >= 2:
    print('El rey negro está en jaque xd')
if fichasNegras >= 2:
    print('El rey blanco está en jaque xd')


