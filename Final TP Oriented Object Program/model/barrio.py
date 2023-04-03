from model.comuna import Comuna
class Barrio():
    def __init__(self, nombre,comuna:Comuna) -> None:
        self.comuna = comuna
        self.nombre = nombre
    

    @property
    def comuna(self):
        return self.__comuna
    
    @comuna.setter
    def comuna(self, valor):
        self.__comuna = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
