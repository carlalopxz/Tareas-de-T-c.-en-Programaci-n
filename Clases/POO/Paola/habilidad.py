class Habilidad():
    def __init__(self,nombre, expertise):
        self.__nombre = nombre
        self.set_expertise(expertise)
    
    def get_nombre(self):
        return self.__nombre
    def get_expertise(self):
        try:
            return self.__expertise
        except AttributeError:
            print("No se creo la habilidad porque el expertise es mayor a 5 o menor que 0")
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_expertise(self,expertise):
        try:
            if expertise <= 5 and expertise >= 0:
                self.__expertise = expertise
        except AttributeError:
            print("No se creo la habilidad porque el expertise era menor a 0 o mayor que 5")