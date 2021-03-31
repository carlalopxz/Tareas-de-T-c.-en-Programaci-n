#Pedir un número entre 0 y 9.999 y mostrarlo con las cifras al revés.

#23 / 10 = 2.3
#23 // 10 = 2
# decena = 23 // 10
# decena = num // 10
# 23 - 2 * 10 = 3
# unidad = num - decena * 10
# print(unidad,decena)

num = int(input('Digite un número del 10 al 9.999 \n'))

if num < 10 or num > 9999:
    print('numero invalido')
else:
    if num < 100:
        decena = num // 10
        unidad = num - decena*10
        print(unidad,decena)
    elif num < 1000:
        centena = num // 100
        decena = (num - centena*100)//10
        unidad = (num - decena*10)-100
        print(unidad,decena,centena)
    elif num < 10000:
        unidadMil = num // 1000
        centena = (num - unidadMil*1000)//100
        decena = (num - (unidadMil * 1000) - (centena * 100)) // 10
        unidad = (num - (unidadMil * 1000) - (centena * 100) - (decena * 10 ))
        print(unidad,decena,centena,unidadMil)
        