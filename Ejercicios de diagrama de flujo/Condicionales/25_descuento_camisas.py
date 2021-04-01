nCamisas = int(input('Ingrese el número de camisas compradas \n'))
precioCamisas = int(input('Ingrese el precio de las camisas \n'))

if nCamisas >= 3:
    descuento = precioCamisas * 0.20
    precioFinal = precioCamisas - descuento
    print('El precio final con el 20% de descuento es de $' + str(precioFinal))
else:
    descuento = precioCamisas * 0.10
    precioFinal = precioCamisas - descuento
    print('El precio final con el 10% de descuento es de $' + str(precioFinal))
