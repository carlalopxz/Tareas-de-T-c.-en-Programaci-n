class CuentaBancaria():
    def __init__(self,nombre,saldo):
        self.__nombre = nombre
        self.__saldo = saldo
    
    def Depositar(self,dinero):
        self.__saldo += dinero
    
    def Extraer(self,dinero):
        self.__saldo -= dinero
    
    def get_MostrarSaldo(self):
        return f"Saldo: {self.__saldo}"
    
    def get_MostrarNombre(self):
        return f"Nombre:{self.__nombre}"

    def set_nombre(self,nombre):
        self.nombre = nombre

cuenta_uno = CuentaBancaria("Carla",0)
print(cuenta_uno.get_MostrarSaldo())
cuenta_uno.Depositar(5000)
print(cuenta_uno.get_MostrarSaldo())
cuenta_uno.Extraer(2000)
print(cuenta_uno.get_MostrarSaldo())
cuenta_uno.set_nombre("Carina")
print(cuenta_uno.get_MostrarNombre())