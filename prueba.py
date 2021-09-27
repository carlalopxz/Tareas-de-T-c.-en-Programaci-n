class Alumno:
    def __init__(self,nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, {self.nombre}")

alumno = Alumno("Carla")
alumno.saludar()
