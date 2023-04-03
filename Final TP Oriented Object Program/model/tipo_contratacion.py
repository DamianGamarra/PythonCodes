class TipoContratacion():
    def __init__(self, descripcion) -> None:
        self.descripcion = descripcion
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor