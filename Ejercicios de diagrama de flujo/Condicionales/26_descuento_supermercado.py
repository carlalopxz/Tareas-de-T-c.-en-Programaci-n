num = int(input('Ingrese un número \n'))
compra = int(input('Ingrese el total de su compra \n'))

if num >= 74:
    descuento = compra * 0.20
    precioF = compra - descuento
    print('El precio final es de $' + str(precioF))
else:
    descuento = compra * 0.15
    precioF = compra - descuento
    print('El precio final es de $' + str(precioF))
    