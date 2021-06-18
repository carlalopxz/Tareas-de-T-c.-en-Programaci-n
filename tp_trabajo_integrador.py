# Diseñar un programa que simule una máquina expendedora de café con un único precio para las opciones, $30. 
# Debe calcular el menor número posible de billetes necesarios para devolver el cambio, teniendo en cuenta 
# que se pueden devolver billetes de 10, 20, 50, 100, 200 pesos. El programa pedirá que se añadan por teclado 
# que billete se introdujo.



while True:
    print('MAQUINA EXPENDORA DE CAFÉ')
    opcion = input('Buenos dias, desea ordenar café? \n A) SI \n B) NO \n El precio del café es de $30. \n').lower()

    def vuelto_compra():
        precioCafé = 30    
        total_compra = 0
        cambio = [10,20,50,100,200]
        cantidad_cafe = int(input('¿Cuántos cafés desea comprar? \n'))
        for cafe in range(cantidad_cafe):
            total_compra += precioCafé
        print(f'Su total de compra es de${total_compra}')
        billete_introducido = int(input('Por favor, introduzca el billete (se aceptan hasta $1000) : '))
        vuelto = billete_introducido - total_compra
        acum_billetes = 0
        if vuelto in cambio:
            print(f'Su vuelto es de ${vuelto}')
        else:
            for billetes in range(len(cambio)):
                print(cambio[-billetes -1])
                

    if opcion == 'a' or opcion == 'si':
        vuelto_compra()
    if opcion == 'b' or opcion == 'no':
        print('Hasta luego :D')
        break
