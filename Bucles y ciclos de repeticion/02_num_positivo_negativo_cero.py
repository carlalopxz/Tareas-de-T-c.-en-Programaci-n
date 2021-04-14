#Leer un número e indicar si es positivo o negativo. 
#El proceso se repetirá hasta que se introduzca un 0.

num = int(input('Ingrese un numero: \n')) #Le pido al usuario un numero que ya define a la variable

while num != 0: #Mientras num sea distinto de cero --> entonces
    if num > 0: #Si num es mayor a cero entonces
        print('Ese numero es positivo') #numero positivo
    elif num < 0: #si no, si num es menor a cero entonces
        print('Ese numero es negativo') #numero negativo
    num = int(input('Ingrese un numero: \n')) #vuelvo a pedirle al usuario un numero
    #asi no entro en un ciclo infinito
print('Es un 0...') #si no se cumple el while es pq num es cero