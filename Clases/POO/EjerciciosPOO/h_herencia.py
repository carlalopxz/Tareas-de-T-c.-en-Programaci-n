class Usuario():
    def __init__(self,nombre,dni,mail):
        self.__nombre = nombre
        self.__dni = dni
        self.__mail = mail

    def get_nombre(self):
        return self.__nombre

class Profesor(Usuario):
    def __init__(self, nombre, dni, mail,matricula):
        super().__init__(nombre, dni, mail)
        self.__matricula = matricula
    def get_matricula(self):
        return self.__matricula

profe1 = Profesor("Carla",41918838,"carlalopez164@gmail.com","175/19")

print(profe1.get_nombre())
print(profe1.get_matricula())