class Celular():
    def __init__(self,marca,modelo,proveedorDeLinea,numero):
        self.__marca = marca
        self.__modelo = modelo
        self.__proveedorDeLinea = proveedorDeLinea
        self.__numero = numero
    
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_proveedor(self):
        return self.__proveedorDeLinea
    def get_numero(self):
        return self.__numero
    
    def set_marca(self,marca):
        self.__marca= marca
    def set_modelo(self,modelo):
        self.__modelo = modelo
    def set_proveedor(self,proveedor):
        self.__proveedorDeLinea = proveedor
    def set_numero(self,numero):
        self.__numero = numero 