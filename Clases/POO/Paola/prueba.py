from usuario import Usuario
from habilidad import Habilidad
from celular import Celular

celular1 = Celular("Motorola","Moto g30","Claro","113456473")
celular2 = Celular("Apple","Iphone 6s","Movistar","1182648822")

habilidad1 = Habilidad("volar",5)
habilidad2 = Habilidad("ser invisible",4)
habilidad3 = Habilidad("comer",3)

usuario1 = Usuario("Paola","paola@gmail.com","perro",celular1)
usuario2 = Usuario("Carla","carla@gmail.com","gato",celular2)

usuario1.saludar()
usuario1.mostrarTelefono()
usuario1.llamar(usuario2,10)

usuario1.agregarHabilidad(habilidad1)
usuario1.agregarHabilidad(habilidad2)
usuario1.agregarHabilidad(habilidad3)
usuario2.agregarHabilidad(habilidad1)
usuario2.agregarHabilidad(habilidad2)
usuario2.agregarHabilidad(habilidad3)

usuario1.saberHacer("ser invisible",4)