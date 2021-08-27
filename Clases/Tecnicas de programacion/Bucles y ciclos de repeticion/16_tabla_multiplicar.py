#Pide un numero (entre 0 y 10)
# mostrar la tabla de multiplicar de dicho numero

num = int(input('Ingrese un numero entre 0 y 10\n'))

for i in range(1,11):
    print(i, ' x ', num, ' = ', (i*num) )
