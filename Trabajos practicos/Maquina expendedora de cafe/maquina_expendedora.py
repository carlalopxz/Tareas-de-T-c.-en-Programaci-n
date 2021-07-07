def pedido():
    total_compra = 0
    precioCafé = 30  
    cantidad_cafe = int(input('¿Cuántos cafés desea comprar? \n'))
    for cafe in range(cantidad_cafe):
        total_compra += precioCafé
    print(f'Su total de compra es de ${total_compra}')
    return total_compra

def cantidadBilletes(vuelto):
    lista_cambio = [200,200,50,20,10]
    diccAcum = {10:0,20:0,50:0,100:0,200:0}
    for i in range(len(lista_cambio)):
        cambio = lista_cambio[i]
        if vuelto == lista_cambio[i]: #200-100-50-20-10
            if cambio == 200:
                diccAcum[200] += 1 
            if cambio == 100:
                diccAcum[100] += 1 
            if cambio == 50:
                diccAcum[50] += 1
            if cambio == 20:
                diccAcum[20] += 1
            if cambio == 10:
                diccAcum[10] += 1
    billetes = {}
    for i in diccAcum.keys():
        if diccAcum[i] != 0:
            billetes[i] = diccAcum[i]
    return billetes

def vuelto_compra(total_compra):  
        billete_introducido = int(input('Por favor, introduzca el billete (se aceptan 10,20,50,100,200) : '))
        if billete_introducido == total_compra:
            print('Disfrute su café')
        if billete_introducido < total_compra:
            dinero_faltante = total_compra - billete_introducido
            print(f'Te faltan {dinero_faltante} para el total de {total_compra}')
            while billete_introducido < total_compra:
                billete = int(input(f'Ingrese el dinero faltante (se aceptan 10,20,50,100,200), tiene {billete_introducido}: '))
                billete_introducido = billete_introducido + billete
            print('Disfrute su café')
            if billete_introducido > total_compra:
                vuelto = billete_introducido - total_compra
                print(f'Su vuelto es de: {vuelto} pesos')
                print(f'Su vuelto se devuelve en estas cantidades {cantidadBilletes(vuelto)}')
        if billete_introducido > total_compra:
            vuelto = billete_introducido - total_compra
            print(f'Su vuelto es de: {vuelto} pesos')
            print(f'Su vuelto se devuelve en estas cantidades {cantidadBilletes(vuelto)}')
        return vuelto 

while True:
    print('MAQUINA EXPENDORA DE CAFÉ')
    opcion = input('Buenos dias, desea ordenar café? \n A) SI \n B) NO \n El precio del café es de $30. \n').lower()
    
    if opcion == 'a' or opcion == 'si':
        totalCompra = pedido()
        vuelto_compra(totalCompra)

    if opcion == 'b' or opcion == 'no':
        print('Hasta luego :D')
        break