#EJERCICIO 7

totalCompra = 0 

print('Digite el total de su compra')
totalCompra = int(input())

descuento = (totalCompra*15)/100

precioFinal = (totalCompra - descuento)

print('El precio final de la compra es de: ' + str(precioFinal) + ' pesos')