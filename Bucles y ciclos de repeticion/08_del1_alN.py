#Ejercicio8.Pedir un número N, y mostrar todos los números del 1 al N.

num = int(input('Ingrese un numero \n')) #Pedir numero al usuario 
mostrar = 1 #variable contadora con valor 1 porque el ejercicio lo pide a partir del 1

while True: #ciclo infinito 
    print(mostrar)  # muestro la variable en cada vuelta 
    mostrar = mostrar + 1 # voy acumulando 1 + 1 ...

    if mostrar == num + 1: # si mostrar es igual a num + 1 (numero que ingreso el usuario mas uno)
        break #break y salgo del ciclo 

#SOLUCION 2 

mostrar = 1

while mostrar != num + 1:
    print(mostrar)
    mostrar = mostrar + 1

#SOLUCION 3

num = int(input('Ingrese un numero \n'))

for i in range(1,num+1):
    print(i)
