#Programar una funcion que muestre en binario un número entre 0 y 255.

#Dividir un numero de manera entera por 2 hasta que el resultado nos de 1.
#Calcular el resto en cada division e ir acumulandolo en una cadena.

#3. Defino una funcion que me convertira un numero en binario
def convertir(decimal):
    #4. Defino una variable 'binario' con una cadena vacia para almacenar los restos 
    binario = ''
    #5. Inicio un WhileTrue
    while True:
        #6. Calculo el resto del numero ingresado
        resto = decimal % 2
        #6.a. Almaceno el resto en 'binario', lo pongo primero para que se concatene al reves 
        binario = str(resto) + binario
        #7. Calculo el numero entero de la division y lo guardo en decimal 
        decimal = decimal // 2
        #8. Si decimal es igual a 1 entonces 
        if decimal == 1:
            #8.a. guardo el decimal en binario y hago un break para que el ciclo while termine
            binario = str(decimal) + binario 
            break
    #9. Devuelvo el resultado de binario
    return binario

#1. Le pido al usuario que ingrese un numero y lo guardo en num
num = int(input('Ingrese un numero para pasar a binario: '))
#2. Llamo a la funcion convertir con el argumento num y guardo lo que devuelve en 'enBinario'
enBinario = convertir(num)
#10. Imprimo lo que devolvio la funcion (binario) a convertir().
print(enBinario)