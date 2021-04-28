#Ejercicio4.Función a la que se le pasan dos enteros y 
# muestra todos los números comprendidos entre ellos, inclusive.

#Ejemplo
#Ingresa 4
#Ingresa 8
#Llamamos a una funcion
#Dentro de la funcion mostramos "4,5,6,7,8"

def mostrarNum(num1,num2):
    for i in range(num1, num2 +1, 1):
        print(i)

num1 = int(input('Ingrese el primer numero \n'))
num2 = int(input('Ingrese el segundo numero \n'))

if num1 > num2:
    mostrarNum(num1,num2)
if num1 < num2:
    mostrarNum(num2,num1)
