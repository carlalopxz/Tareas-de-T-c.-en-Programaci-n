class CuentaBancaria():
    def __init__(self,numero,titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
    
    def get_nombre(self):
        return self.__titular.get_nombre()
    def get_saldo(self):
        return self.__saldo

    def set_cargarSaldo(self,numero):
        self.__saldo += numero

    def tranferencia(self,monto,cuenta):
        cuenta.set_cargarSaldo(monto)
        self.__saldo -= monto

