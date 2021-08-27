#Diseña una función que decida si un número es primo. 

#4. Defino una funcion que me dice si numero es divisible por i 
def esDivisible (a,b):
    #4.a. Si a modulo b me da cero devuelvo True
    if a%b == 0 :
        return True
    #4.b. Si no devuelvo False 
    else: 
        return False

def aumentar() :
    #5. Accedo a la variable global contador
    global contador
    #5.a. Aumento contador en 1 y lo guardo en contador
    contador = contador +1

#3. En la funcion esPrimo se copia el num en numero
def esPrimo(numero):
    #3.a. Accedo a la variable global contador 
    global contador
    #3.b Para i en un rango que comienza en uno y termina en numero + 1 (el numero q ingreso el usuario se incluye)
    for i in range(1,numero+1):
        #3.c. Llamo a la funcion esDivisible con los argumentos numero (con el numero q ingreso el usuario) e i (1,2,3,4...)
        #3.d. Si la funcion esDivisible me devuelve True llamo a la funcion aumentar()       
        if esDivisible(numero,i):
            aumentar()
    #6. Despues de llamar a la funcion aumentar, me fijo si contador vale mas que dos o es igual a 2
    if contador > 2:
        return False #No es primo porque tiene mas de 2 divisores
    elif contador == 2:
        return True #Es primo porque tiene 2 divisores
contador = 0
#1. Le pido al usuario que ingrese un numero y lo guardo en num 
num = int(input('Ingrese un numero para ver si es Primo'))
#2. Llamo a la funcion esPrimo con el argumento num  
if esPrimo(num):
    #2.a. Si da True se ejecuta este print
    print(str(num)+' es primo.')
else:
    #2.b. Si da False se ejecuta este print
    print(str(num)+' no es primo.')