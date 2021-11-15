from abc import ABC,abstractmethod

class Cuenta(ABC):
    def __init__(self,CBU,balance,fechaUltimoMovimiento):
        self.__CBU = CBU
        self.__balance = balance
        self.__fechaUltimoMovimiento = fechaUltimoMovimiento
    
    def get_CBU(self):
        return self.__CBU
    def get_balance(self):
        return self.__balance
    def get_fechaUltimoMovimiento(self):
        return self.__fechaUltimoMovimiento
    
    def set_CBU(self,CBU):
        self.__CBU = CBU
    def set_balance(self,balance):
        self.__balance = balance
    def set_fechaUltimoMovimiento(self,fechaNueva):
        self.__fechaUltimoMovimiento = fechaNueva

    @abstractmethod

    def transaccion(self,monto,cajero):
        pass 