class Articulo():
    def __init__(self, nombreArticulo,precioArticulo):
        self.__nombreArticulo = nombreArticulo
        self.__precioArticulo = precioArticulo
    
    #Getters
    def get_nombreArt(self):
        return self.__nombreArticulo
    def get_precioArt(self):
        return self.__precioArticulo
    #Setters 
    def set_nombreArt(self,nombre):
        self.__nombreArticulo = nombre
    def set_precioArt(self,precio):
        self.__precioArticulo = precio

class ArticuloJardin(Articulo):
    def __init__(self, nombreArticulo, precioArticulo,esProfesional):
        super().__init__(nombreArticulo, precioArticulo)
        self.__esProfesional = esProfesional
    #Getters
    def get_esProfesional(self):
        return self.__esProfesional
    #Setter
    def set_esProfesional(self,esProfesional):
        self.__esProfesional = esProfesional

class Juguete(Articulo):
    def __init__(self, nombreArticulo, precioArticulo,edadRecomendada):
        super().__init__(nombreArticulo, precioArticulo)
        self.__edadRecomendada = edadRecomendada
    #Getters
    def get_edadRecomendada(self):
        return self.__edadRecomendada
    #Setters
    def set_edadRecomendada(self,edadNueva):
        self.__edadRecomendada = edadNueva
    
class Vajilla(Articulo):
    def __init__(self, nombreArticulo, precioArticulo,matConfeccion,tipoVajilla):
        super().__init__(nombreArticulo, precioArticulo)
        self.__matConfeccion = matConfeccion
        self.__tipoVajilla = tipoVajilla
    #Getters
    def get_matConfeccion(self):
        return self.__matConfeccion
    def get_tipoVajilla(self):
        return self.__tipoVajilla
    #Setters
    def set_matConfeccion(self,materialNuevo):
        self.__matConfeccion = materialNuevo
    def set_tipoVajilla(self,tipoNuevo):
        self.__tipoVajilla = tipoNuevo
    