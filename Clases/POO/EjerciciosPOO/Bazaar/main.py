from personal import empleadoComun, empleadoMostrador, Repositor, Coordinador
from articulo import Vajilla, ArticuloJardin,Juguete
from bazaar import Bazaar

#Instancias de Empleados 
empleado_uno = empleadoComun("Carina","Lopez","12640596",20000,0)
empleado_dos = Repositor("Graciela","Martines","18987654",20000,0)
empleado_tres = empleadoMostrador("Rolando","Lopez","12765356",20000,0)
empleado_cuatro = Coordinador("Juan","El cacas","7529764",40000,0)
#Instancias de Bazaar
bazzar_uno = Bazaar("Bazaar Online","Ginebra 3000","Perez, Juan","Lopez, Carla")
#Instancias de Articulos
articulo_uno = Juguete("Muñeca",450,2)
articulo_dos = Vajilla("Plato",345,"Ceramica","Plato playo")
articulo_tres = ArticuloJardin("Pala",789,True)
#Agregar empleados al bazaar
bazzar_uno.agregarEmpleado(empleado_uno)
bazzar_uno.agregarEmpleado(empleado_dos)
bazzar_uno.agregarEmpleado(empleado_tres)
bazzar_uno.agregarEmpleado(empleado_cuatro)
#Agregar articulos al bazaar
bazzar_uno.agregarArticulo(articulo_uno)
bazzar_uno.agregarArticulo(articulo_dos)
bazzar_uno.agregarArticulo(articulo_tres)
#Agregar articulos al deposito
bazzar_uno.agregarAlDeposito(articulo_uno)
bazzar_uno.agregarAlDeposito(articulo_uno)
bazzar_uno.agregarAlDeposito(articulo_dos)
bazzar_uno.agregarAlDeposito(articulo_tres)
bazzar_uno.agregarAlDeposito(articulo_tres)

print("------------PRUEBA BAZAAR------------")
print(f"Nombre bazaar: {bazzar_uno.get_nombre()}")
print(f"Direccion de {bazzar_uno.get_nombre()}: {bazzar_uno.get_direccion()}")
print(f"Dueño de {bazzar_uno.get_nombre()}: {bazzar_uno.get_duenio()}")
print(f"Gerente de {bazzar_uno.get_nombre()}: {bazzar_uno.get_gerente()}")
print(f"Numero de empleados de {bazzar_uno.get_nombre()}: {bazzar_uno.contarEmpleados()}")
print(f"Numero de articulos de {bazzar_uno.get_nombre()}: {bazzar_uno.stock()}")
print(f"Empleados de {bazzar_uno.get_nombre()}")
bazzar_uno.listarEmpleados()
bazzar_uno.mostrarDeposito()

print("------------PRUEBA ARTICULOS------------")
print("-----PRUEBA JUGUETES-----")
articulo_uno.mostrarArticulos()
print("-----PRUEBA VAJILLA-----")
articulo_dos.mostrarArticulos()
print("-----PRUEBA ART.JARDIN-----")
articulo_tres.mostrarArticulos()

print("------------PRUEBA EMPLEADOS------------")
print("-----PRUEBA EMPLEADO COMUN-----")
empleado_uno.venderArticulo(bazzar_uno,articulo_uno)
print(f"Comision despues de vender: {empleado_uno.get_comision()}")
print("-----PRUEBA EMPLEADO MOSTRADOR----")
print(f"Dinero disponible antes de la venta: {empleado_tres.get_caja()}")
empleado_tres.cobrar(articulo_uno)
print(f"Dinero disponible despues de la venta: {empleado_tres.get_caja()}")
print("-----PRUEBA REPOSITOR-----")
print(f"Stock: {bazzar_uno.stock()}")
#bazzar_uno.mostrarDeposito()
empleado_dos.irDeposito(articulo_tres,bazzar_uno)
print(f"Stock: {bazzar_uno.stock()}")
#bazzar_uno.mostrarDeposito()
print("-----PRUEBA COORDINADOR-----")
empleado_cuatro.coordinarEmpleados()

print("-----LIQUIDACION DE SUELDOS-----")
bazzar_uno.liquidarSueldo()