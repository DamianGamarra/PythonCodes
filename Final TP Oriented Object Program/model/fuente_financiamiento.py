class FuenteFinanciamiento():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
