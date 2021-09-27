import datetime

class Pelicula:
    def __init__(self, id, titulo, fecha_de_estreno):
        self.id=id
        self.titulo=titulo
        self.fecha_de_estreno=fecha_de_estreno

    def Reproducir(self):
        print(f"Reproduciendo a {self.titulo}")

    #def Describir(self):
    #    print(f"{self.titulo}:{self.rating}")

    #def ratingMayorA(self,numero):
    #    if self.rating>numero:
    #        return True
    #    else:
    #        return False
    def get_id(self):
        return self.id
    def get_titulo(self):
        return self.titulo
    #def get_rating(self):
    #    return self.rating
    def get_fecha_de_estreno(self):
        return self.fecha_de_estreno

    def set_id(self,id):
        self.id=id
    def set_titulo(self,titulo):
        self.titulo=titulo
    def set_rating(self,rating):
        if rating >0 and rating <=10:
            self.rating=rating
    def set_fecha_dr_estreno(self,fecha_de_estreno):
        self.fecha_de_estreno=fecha_de_estreno

ToyStory=Pelicula(1,"ToyStory",datetime.datetime(2018, 6, 1))
BuscandoANemo=Pelicula(2,"Buscando a Nemo",datetime.datetime(2020, 8, 1))


print(BuscandoANemo.get_fecha_de_estreno())