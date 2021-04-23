#Pedir 10 números.
#Mostrar la media de los números positivos,
# la media de los números negativos
# y la cantidad de ceros ingresados. 

#Promedio = Suma / Cantidad

num = ''
cont = 0 
sumaPositivos = 0
for i in range(1,11):
    num = int(input('Ingrese un numero \n'))

    while True:
        if num > 0:
            break
        sumaPositivos = sumaPositivos + num
        cont = cont + 1
        print('Suma de los numeros: '+str(sumaPositivos))
        print('Promedio de los numeros: '+str(int(sumaPositivos/cont)))
