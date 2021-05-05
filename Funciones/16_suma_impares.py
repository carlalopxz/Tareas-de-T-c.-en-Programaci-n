#Escriba una función que sume los n primeros números impares.

def suma_impares():
    global n
    suma = 1
    for i in range(1,n+1,2):
        suma = suma + i
    return suma

n = int(input('Ingres en número N \n'))  

print('La suma de los numeros impares es:'+str(suma_impares()))
