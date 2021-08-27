#Pedir un nùmero entre 0 y 9999 y decir cuantas cifras tiene.

num = input('Digite un numero del 0 al 9999 \n')

print('El nùmero tiene ' + str(len(num)) + ' cifras ')

#OPCION 2

num = int(input('Digite un numero del 0 al 9999 \n'))

if num < 0 or num > 9999:
    print('numero invalido')
elif num < 10:
    print('El numero ' + str(num) + ' tiene 1 cifra')
elif num < 100:
    print('El numero ' + str(num) + ' tiene 2 cifras')
elif num < 1000:
    print('El numero ' + str(num) + ' tiene 3 cifras')
elif num < 10000:
    print('El numero ' + str(num) + ' tiene 4 cifras')