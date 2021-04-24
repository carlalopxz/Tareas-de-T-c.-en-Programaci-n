#Pedir 15 números y escribir la suma total, y calcular el promedio. 

suma = 0
cont = 0
for i in range (15):
    num = int(input('Digite un numero \n'))
    suma = suma + num
    cont = cont + 1
print(suma)
print(suma/cont) #print(suma/15)