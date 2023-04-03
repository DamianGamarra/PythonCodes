class Comuna():
    def __init__(self,numero) -> None:
        self.numero = numero

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self,valor):
        self.__numero = valor
        
