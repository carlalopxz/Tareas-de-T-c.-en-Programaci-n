# Diseñar una función que tenga como parámetros dos números, y 
# que calcule el maximo entre 3 números. 

def numMax(num1,num2):

    if num1 > num2:
        maximo = num1
    elif num1 < num2:
        maximo = num2
    else:
        print('Los dos numeros son iguales')
    
    return maximo

num1 = int(input('Ingrese el primer numero \n'))
num2 = int(input('Ingrese el segundo numero \n'))

maximo = numMax(num1,num2)

print('El maximo es: ' + str(maximo))