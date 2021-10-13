class Bazaar():
    def __init__(self,nombre, direccion,duenio,gerente):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__duenio = duenio
        self.__gerente = gerente
        self.__empleados = []
        self.__articulos = []
        self.__deposito = []
    
    #Getters
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_duenio(self):
        return self.__duenio
    def get_gerente(self):
        return self.__gerente
    def get_caja(self):
        return self.__caja
    #Setters
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_direccion(self,direccion):
        self.__direccion = direccion
    def set_duenio(self,duenio):
        self.__duenio = duenio
    #Metodos
    def liquidarSueldo(self):
        sueldoTotal = 0
        for i in self.__empleados:
            sueldoTotal += (i.get_sueldo() + i.get_comision())
        print(f"Sueldo total: {sueldoTotal}")
    def contarEmpleados(self):
        return len(self.__empleados)
    def agregarEmpleado(self,empleado):
        self.__empleados.append(empleado)
    def eliminarEmpleado(self,empleado):
        self.__empleados.remove(empleado)
    def listarEmpleados(self):
        for i in self.__empleados:
            print(f"Nombre: {i.get_nombre()} | Apellido: {i.get_apellido()} | DNI: {i.get_dni()} | Sueldo: {i.get_sueldo()}")
    def agregarArticulo(self,articulo):
        self.__articulos.append(articulo)
    def eliminarArticulo(self,articulo):
        self.__articulos.remove(articulo)
    def stock(self):
        return len(self.__articulos)
    def agregarAlDeposito(self,articulo):
        self.__deposito.append(articulo)
    def mostrarDeposito(self):
        for i in self.__deposito:
            print(f"{i.mostrarArticulos()}")
