from personal import Personal

class empleadoMostrador(Personal):
    def __init__(self, nombre, apellido, dni, sueldo, comision):
        super().__init__(nombre, apellido, dni, sueldo, comision)

    #Metodos
    def cobrar(self,articulo):
        pass
    def sumarDineroCaja(self,articulo):
        pass
    def restarDineroCaja(self):
        pass
    