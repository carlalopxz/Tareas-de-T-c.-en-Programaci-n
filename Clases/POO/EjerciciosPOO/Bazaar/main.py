from personal import Personal
from art_jardin import ArticuloJardin
from juguete import Juguete
from articulo import Articulo
from bazaar import Bazaar
from vajilla import Vajilla

bazaar1 = Bazaar("Bazzar","Ginebra 354","Carla","Carina")
Articulo1 = Articulo("Plato",500)
ArticuloVajilla = Vajilla(Articulo1.get_nombreArt(),Articulo1.get_precioArt(),"Ceramica","Plato")
Articulo2 = Articulo("Muñeca",600)
juguete = Juguete(Articulo2.get_nombreArt(),Articulo2.get_precioArt(),2)
articulo3 = Articulo("Pala",500)
pala = ArticuloJardin(articulo3.get_nombreArt(),articulo3.get_precioArt(),True)
bazaar1.agregarArticulo(ArticuloVajilla)
bazaar1.agregarArticulo(juguete)
bazaar1.agregarArticulo(pala)
bazaar1.mostrarArticulos()

print(f"Numero de empleados {bazaar1.get_numEmpleados()}")
print(f"Dueño: {bazaar1.get_duenio()}")
print(f"{pala.get_esProfesional()}")

persona1 = Personal("juan","perez","27987786",20000,0)
bazaar1.agregarEmpleado(persona1)
print(bazaar1.contarEmpleados())