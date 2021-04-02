llantas = int(input('Ingrese la cantidad de llantas compradas \n'))

if llantas >= 5:
    precioF = llantas * 700
    print('El precio final es de $' + str(precioF))
else:
    precioF = llantas * 800
    print('El precio final es de $' + str(precioF))
