from f_relaciones import CuentaBancaria

class Titular():
    def __init__(self,nombre,dni):
        self.__nombre = nombre 
        self.__dni = dni
    
    def get_nombre(self):
        return self.__nombre
    def get_dni(self):
        return self.__dni
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_dni(self,dni):
        self.__dni = dni
    
titular_uno = Titular("Carla",41918838)
cuenta_uno = CuentaBancaria(1,titular_uno,)

titular_dos = Titular("Carina",12640596)
#relacion de composicion 
cuenta_dos  =CuentaBancaria(2,titular_dos)

print(cuenta_uno.get_nombre())

cuenta_uno.set_cargarSaldo(5000)
print(cuenta_uno.get_saldo())
print(cuenta_dos.get_saldo())
#relacion de agregacion 
cuenta_uno.tranferencia(2000,cuenta_dos)
print(cuenta_uno.get_saldo())
print(cuenta_dos.get_saldo())