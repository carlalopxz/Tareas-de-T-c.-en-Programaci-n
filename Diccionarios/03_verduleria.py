# Ejercicio3. Escribir un programa que contenga en un diccionario los precios de una verdulería. 
# El programa pedirá el nombre de la verdura y la cantidad que se ha vendido y nos mostrará el precio final
# de la venta a partir de los datos guardados en el diccionario. Si la verdura no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

#Por ejemplo:
#precioVerduras = {'Apio':2}
#nomVerdura = 'Apio'
#vendimos = 23
#precioFinal = 46
#Desea hacer otra consulta/compra.
#nomVerdura = 'Lechuga'
#caso que no exista 'Error no está en venta'
#Desea hacer otra consulta/compra.

#BIENVENIDO A LA VERDULERIA DE FULANITO
#A ) Deseo hacer una compra 
#B ) Quiero irme 

#print("\033[H\033[J")

verduras_del_menu = {'Cebolla verdeo':10,'Apio':20, 'Cebolla':30,'Zapallo': 40,'Papas':50,'Zanahoria':60,'Maiz':70}
Opcion = input('Hola, Bienvenido a nuestra verduleria, seleccione una opcion para empezar: \n A) Deseo comprar \n B) Deseo salir \n').lower()
verdurasElegidas = {}

def compra_en_verduleria(numDeVerduras):
    totalDeCompra = 0
    print(f'Hola, le muestro nuestras verduras disponibles y el precio por cantidad: {verduras_del_menu}')
    if numDeVerduras > 0:
        for i in range(numDeVerduras):
            verduras_compradas = input('Muy bien, digame que verduras desea comprar: \n')
            cantidad_verduras = int(input(f'¿Qué cantidad de {verduras_compradas} desea comprar?: '))
            if verduras_compradas in verduras_del_menu.keys():
                verdurasElegidas[verduras_compradas] = cantidad_verduras
            else:
                print('No tenemos esa verdura a la venta NEE')
            totalDeCompra = totalDeCompra +  cantidad_verduras * verduras_del_menu[verduras_compradas]
    print(f'Las verduras y la cantidad que compró son: {verdurasElegidas}')
    print(f'El precio total de las verduras que compró es: ${totalDeCompra}')
        
if Opcion == 'a':
    numDeVerdurasAComprar = int(input('¿Cuantas verduras desea comprar?'))
    compra_en_verduleria(numDeVerdurasAComprar)
if Opcion == 'b':
    print('Un gusto que haya pasado por nuestra verduleria')

#Solucion 2 

precios = {"brocoli": 2, "lechuga": 5, "papa": 4, "tomate": 3}
while True:
    verdura = input("Dime la verdura que vendi:").lower()
    if verdura not in precios:
        print("Verdura no existe.")
    else:
        cantidad = int(input("Dime la cantidad de verdura que vendi:"))
        print("El precio final de esta venta:" + str(cantidad * precios[verdura]))
    opcion = input("¿Quieres vender otra verdura (s/n)").lower()
    while opcion[0] != "s" and opcion[0] != "n":
        opcion = input("¿Quieres vender otra verdura (s/n)")
    if opcion[0] == "n":
        break
 
