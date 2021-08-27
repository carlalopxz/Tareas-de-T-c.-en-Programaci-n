#Escriba una función que sume los n primeros números impares.

def suma_impares():
    global n
    suma = 0
    for i in range(1,n,2):
        suma = suma + i
    return suma

n = int(input('Ingrese en número N \n'))  

print('La suma de los numeros impares es: '+str(suma_impares()))
