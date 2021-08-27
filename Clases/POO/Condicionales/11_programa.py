"""
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número 
que se escoge al azar. Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, 
si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta
"""

num = int(input('Ingrese un número \n'))
compra = int(input('Ingrese el total de su compra \n'))

if num >= 74:
    descuento = compra * 0.20
    precioF = compra - descuento
    print(f'El precio final es de ${precioF}')
else:
    descuento = compra * 0.15
    precioF = compra - descuento
    print(f'El precio final es de ${precioF}')