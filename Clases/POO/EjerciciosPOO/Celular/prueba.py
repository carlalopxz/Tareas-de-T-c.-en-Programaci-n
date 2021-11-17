from usuario import Usuario
from celular import Celular
from base import BD

celularUno = Celular("Apple","Iphone 6s","Movistar","367492749")
celularDos = Celular("Motorola","Moto G30","Claro","57648373")
celularTres = Celular("Apple","Iphone 6s","Movistar","3674545549")

usuarioUno = Usuario("Carla","carla@live.com","prueba123!",celularUno,1)
usuarioDos = Usuario("Carina","cari@live.com","pedroychiquito",celularDos,2)
usuarioTres = Usuario("Gra","gra@live.com","mueble123",celularTres,3)

usuarioUno.saludar()
print(usuarioUno.get_contrasenia())

print(usuarioDos.get_celular().get_marca())

print("----Datos del telefono----")
usuarioUno.mostrarTelefono()
print("----Llamada----")
usuarioUno.llamar(usuarioTres,4)
usuarioUno.llamar(usuarioDos,10)
print("----Metodo Guardar----")
usuarioDos.guardar(usuarioTres)
usuarioUno.guardar(usuarioDos)
print("----Metodo Eliminar----")
usuarioUno.eliminar(usuarioDos)

celular1 = Celular("Motorola","Moto G30","Claro","11763367467")
