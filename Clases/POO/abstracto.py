from abc import ABC,abstractmethod #libreria para definir clases y metodos abstractos

class Articulo(ABC):
    def __init__(self,nombre,precio):
        self.__nombre = nombre
        self.__precio = precio
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_precio(self,precio):
        self.__precio = precio
# DECORADOR: Bloque de funciones donde abajo de un decorador puede seguir definiendo otro tipo de funciones 
# le da limitaciones al bloque de codigo que sigue abajo del decorador   
    @abstractmethod
    # Abstract Method: Determina que me deje definir los metodos abstractos
    def mostrarArticulos(self):
        pass

class Juguete(Articulo):
    def __init__(self, nombre, precio,edad):
        super().__init__(nombre, precio)
        self.__edad = edad
    #Getters
    def get_edad(self):
        return self.__edad
    #Setters
    def set_edad(self,edad):
        self.__edad = edad
    #Metodos 
    def mostrarArticulos(self):
        print(f"El articulo es {self.get_nombre()}, su precio es de {self.get_precio()} y es para chicos de {self.get_edad()} años")

articulo_uno = Juguete("Panda Peluche",500,2)
articulo_uno.mostrarArticulos()


