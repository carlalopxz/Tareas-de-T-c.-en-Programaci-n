#Pedir un número entre 0 y 9.999, decir si es capicúa.
#3113
#3113
#212
#212

num = int(input('Digite un número del 0 al 9.999 \n'))

if num < 0 or num > 9999:
    print('numero invalido')
else:
    if num < 10:
        print('El numero ' + str(num) + ' es capicua')
    elif num < 100:
        decena = num // 10
        unidad = num - decena*10
        if decena == unidad:
            print('El numero ' + str(num) + ' es capicua')
        else:
            print('El numero ' + str(num) + ' no es capicua')
    elif num < 1000:
        centena = num  // 100 
        decena = (num - centena*100) // 10
        unidad = num - centena*100 - decena*10
        if centena == unidad:
            print('El numero ' + str(num) + ' es capicua')
        else:
            print('El numero ' + str(num) + ' no es capicua')
    else: #elif num < 10000:
        unidadMil = num // 1000
        centena = (num - unidadMil*1000)//100
        decena = (num - (unidadMil * 1000) - (centena * 100)) // 10
        unidad = (num - (unidadMil * 1000) - (centena * 100) - (decena * 10 ))
        if unidadMil == unidad and centena == decena:
            print('El numero ' + str(num) + ' es capicua')
        else:
            print('El numero ' + str(num) + ' no es capicua')