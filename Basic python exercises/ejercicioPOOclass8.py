#Ejercicio de la clase 8 de programación orientada a objetos a partir de un diagrama UML.
from abc import ABC, abstractmethod


class Cliente:

    def __init__(self,razon_social:str, cuil:int, domicilio:str) -> None:
        print("Iniciando instancia Cliente.")
        self.razon_social = razon_social
        self.cuil = cuil
        self.domicilio = domicilio


    @property
    def razon_social(self):
        return self.__razon_social

    @razon_social.setter
    def razon_social(self,razon_social):
        self.__razon_social = razon_social

    @property
    def cuil(self):
        return self.__cuil

    @cuil.setter
    def cuil(self,cuil):
        self.__cuil = cuil
    
    @property
    def domicilio(self):
        return self.__domicilio

    @cuil.setter
    def domicilio(self,domicilio):
        self.__domicilio = domicilio

    def crear_cuenta_bancaria(self, tipo_cuenta:str, nro_cuenta:int,titular, saldo:float) -> bool:
        if tipo_cuenta == "CA":
            return CajaAhorro(nro_cuenta,titular,saldo)
        elif tipo_cuenta == "CC":
            return CuentaCorriente(nro_cuenta,titular,saldo)
    



class CuentaBancaria(ABC):

    def __init__ (self, nro_cuenta:int, titular:Cliente,saldo:float) -> None:
        self.nro_cuenta = nro_cuenta
        self.titular = titular
        self.saldo = saldo

    @property
    def nro_cuenta(self):
        return self.__nro_cuenta

    @nro_cuenta.setter
    def nro_cuenta(self,nro_cuenta):
        self.__nro_cuenta = nro_cuenta
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo


    def consultar_saldo(self) -> float:
        print('Consultando el saldo.')
        return self.__saldo

    def depositar(self,monto_depositar:float) -> bool:
        self.saldo = self.saldo + monto_depositar

    def consultar_cliente(self) -> str:
        return 'el cliente es: ' + self.__titular


    @abstractmethod
    def extraer(self,monto_extraer:float) -> bool:
        pass

    @abstractmethod
    def transferir(self,monto_transferir:float) -> bool:
        pass


class ExtraerExcepcion(Exception):
    def __init__(self, mensaje) :
        super().__init__(mensaje)
    



class CajaAhorro(CuentaBancaria):
    
    def __init__(self, nro_cuenta, titular, saldo, limite_extracciones:float = 30000, cant_extracciones:float= 10) -> None:
        super().__init__(nro_cuenta,titular,saldo)
        print("Instancia Caja Ahorro")
        self.limite_extracciones = limite_extracciones
        self.cant_extracciones = cant_extracciones

    @property
    def limite_extracciones(self):
        return self.__limite_extracciones

    @limite_extracciones.setter
    def limite_extracciones(self,limite_extracciones):
        self.__limite_extracciones = limite_extracciones

    @property
    def cant_extracciones(self):
        return self.__cant_extracciones

    @cant_extracciones.setter
    def cant_extracciones(self,cant_extracciones):
        self.__cant_extracciones = cant_extracciones

    
    def extraer(self,monto_extraer:float) -> bool:
        if monto_extraer > self.saldo or monto_extraer > self.limite_extracciones:
            raise ExtraerExcepcion ("No se pudo realizar la extracción en CajaAhorro")

        else:
            self.saldo = self.saldo - monto_extraer
            print('Extracción exitosa')
            return True 


    def transferir(self, monto_transferir:float) -> bool:
        if monto_transferir > self.saldo:
            print('Error, no puede transferir ese monto')
            return False
        else:
            self.saldo = self.saldo - monto_transferir
            print('Transferencia exitosa')
            return True





class CuentaCorriente(CuentaBancaria):

    def __init__(self, nro_cuenta:int , titular ,saldo:float,monto_descubierto:float=50000) -> None:
        super().__init__(nro_cuenta,titular,saldo)
        print("Instancia Cuenta Corriente")
        self.monto_descubierto = monto_descubierto

    @property
    def monto_descubierto(self):
        return self.__monto_descubierto

    @monto_descubierto.setter
    def monto_descubierto(self, valor):
        if valor > 0 :
            self.__monto_descubierto = valor
        else:
            print("No se puede asignar un valor negativo al monto descubierto.")


    def extraer(self,monto_extraer:float) -> bool:
        if monto_extraer > self.saldo + self.monto_descubierto:

            raise ExtraerExcepcion ("No se pudo realizar la extracción en Cuenta Corriente")
        else:
            self.saldo = self.saldo - monto_extraer
            print('Extracción exitosa')
            return True
            
    def transferir(self,monto_transferir:float) -> bool:
        if monto_transferir > self.saldo + self.monto_descubierto:
            print('Error, no puede transferir ese monto')
            return False
        else:
            self.saldo = self.saldo - monto_transferir
            print('Transferencia exitosa')
            return True

#En el main realizamos pruebas de los métodos para ver si funcionan y los errores del código.
def main():

    
    cliente1 = Cliente('Giganet', 20922929, 'Av Corrientes 4500')
    print(cliente1)

    cuenta1 = cliente1.crear_cuenta_bancaria('CA', 20010, cliente1, 2)
    cuenta2 = cliente1.crear_cuenta_bancaria('CC', 20010, cliente1, 30)

    print('Saldo actual: ', cuenta1.consultar_saldo())
    cuenta1.depositar(500920)
    print('Saldo actual CA: ', cuenta1.consultar_saldo())
    cuenta1.extraer(50022920)
    print('Saldo actual CA: ', cuenta1.consultar_saldo())
    
    print('Saldo actual CC: ', cuenta2.consultar_saldo())
    cuenta2.monto_descubierto = -300
    #cuenta2.extraer(400)
    print('Saldo actual CC: ', cuenta2.consultar_saldo())
    cuenta2.transferir(580)
    print('Saldo actual CC: ', cuenta2.consultar_saldo())



main()
