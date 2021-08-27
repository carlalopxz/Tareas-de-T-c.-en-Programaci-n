#Ejercicio1.Pedir un número y mostrar su cuadrado, 
#repetir el proceso hasta que se introduzca un número negativo. 

num = 0 #declaro una variable antes porque en While 
#no puedo poner como condicion variabbles no declaradas.
while num >=0: #Mientras num sea mayor o igual a cero
    num = int(input('Ingrese un número \n')) #Pido al usuario un numero
    print(num**2) #Muestro el cuadrado
print('Se ingreso un número negativo.') #Si el usuario ingreso un numero negativo lo digo
print('Fin del programa') # y terminar el programa 