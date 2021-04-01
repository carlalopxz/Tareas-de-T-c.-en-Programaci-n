#EJERCICIO 2

gradosC = 0
gradosF = 0 

gradosC = int(input('Ingrese un valor de °C del 0 al 100'))

def conversion(gradosC):
    return (9/5*gradosC)+32

print(str(conversion(gradosC)))