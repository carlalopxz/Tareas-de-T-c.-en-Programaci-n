def printCajas(simbolo,ancho,altura):
    if len(simbolo) !=1:
        raise Exception('El simbolo solo puede ser 1 caracter.')
    if ancho <= 2:
        raise Exception('El ancho debe ser mas grande que 2.')
    if altura <= 2:
        raise Exception('La altura debe ser mas graned que 2.')
    print(simbolo * ancho)
    for i in range(altura-2):
        print(simbolo + (' ' * (ancho - 2) + simbolo))
        print(simbolo * ancho)

for sym,w,h in (('*',4,4),('O',20,5),('X',1,3),('ZZ',3,3)):
    try:
        printCajas(sym,w,h)
    except Exception as err:
        print('Una excepcion ocurrio ' + str(err))
