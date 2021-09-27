class Pelicula: #Clase 
    def __init__(self,id,titulo,rating,fecha_estreno): #Constructor 
        self.__id = id
        self.__titulo = titulo
        self.__rating = rating
        self.__fecha_estreno = fecha_estreno
        
    #metodo 
    def reproducir(self):
        return f"Reproduciendo {self.__titulo}"
    #metodo
    def describirse(self):
        return f"{self.__titulo}: {self.__rating} de rating"
    #metodo
    def ratingMayorA(self,rating):
        return self.__rating > rating
    
    #Getters
    def getId(self):
        return self.__id
    def getTitulo(self):
        return self.__titulo
    def getRating(self):
        return self.__rating
    def getFechaEstreno(self):
        return self.__fecha_estreno
    def getNombreGenero(self):
        return self.__genero.getNombre()
    #Setters
    def setId(self,id):
        self.__id = id
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def setRanting(self,rating):
        """
        if rating < 0:
            self.rating = 0
        elif rating > 10:
            self.rating = 10
        else:
            self.rating = rating"""
        self.__rating = min(max(rating,0),10)
        #min = compara los num, elige el menor
        #max = comprar los num, elige el mayor
    def setFechaEstreno(self,fecha_estreno):
        self.__fecha_estreno = fecha_estreno
    def setGenero(self,genero):
        self.__genero = genero

class Genero:
    def __init__(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

#Instancias, instanciar clases 
#mipeli = Pelicula() 
toyStory = Pelicula(None,"Toy Story",9.5,None)
buscandoANemo = Pelicula(2,"Buscando a Nemo",8.7,None)
#llamando al metodo reproducir del objeto pelicula toy story
print(toyStory.reproducir()) 
print(buscandoANemo.reproducir())
#Llamando al metodo describirse
print(toyStory.describirse())
print(buscandoANemo.describirse())
#llamando al metodo ratingmayora
print(f"Es buena la peli? {toyStory.ratingMayorA(5)}")
print(f"Es buena la peli? {toyStory.ratingMayorA(10)}")
#Lllamando a los getters
print("TOY STORY GETTERS")
print(toyStory.getId())
print(toyStory.getTitulo())
print(toyStory.getRating())
print(toyStory.getFechaEstreno())
print("BUSCANDO A NEMO GETTERS")
print(buscandoANemo.getId())
print(buscandoANemo.getTitulo())
print(buscandoANemo.getRating())
print(buscandoANemo.getFechaEstreno())
print("SETTERS")
toyStory.setRanting(16)
buscandoANemo.setRanting(-4)
print(f"Rating modificado: {toyStory.getTitulo()} :{toyStory.getRating()}")
print(f"Rating modificado: {buscandoANemo.getTitulo()}: {buscandoANemo.getRating()}")
#Clase Genero
animacion = Genero("Animacion")
toyStory.setGenero(animacion)
buscandoANemo.setGenero(animacion)

print(f"Genero de {toyStory.getTitulo()}: {toyStory.getNombreGenero()}")
print(f"Genero de {buscandoANemo.getTitulo()}: {buscandoANemo.getNombreGenero()}")