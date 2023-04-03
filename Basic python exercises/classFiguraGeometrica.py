import math
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    
    def __init__ (self, color_fondo ,color_borde):
        print("Soy el constructor de FiguraGeometrica")
        self.color_fondo = color_fondo
        self.color_borde = color_borde

    @property
    def color_fondo(self) :
        return self.__color_fondo


    @color_fondo.setter
    def color_fondo(self, color) :
        self.__color_fondo = color

    @property
    def color_borde(self) :
        return self.__color_borde
    
    @color_borde.setter
    def color_borde(self, color):
        self.__color_borde = color

    @abstractmethod
    def area(self) ->float:
        pass

    @abstractmethod
    def perimetro(self) ->float:
        pass


class Rectangulo(FiguraGeometrica):

    def __init__(self, base:float, altura:float,color_fondo,color_borde):
        print("Soy el constructor de Rectangulo")
        super().__init__(color_fondo, color_borde)

        self.base = base
        self.altura = altura


    @property
    def base(self) :
        return self.__base

    @base.setter
    def base(self,base):
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura



    def area(self) -> float :
        print("Soy el area del rectangulo")
        return self.base * self.altura
    
    def perimetro(self) -> float:
        print("Soy el perimetro del rectangulo")
        return 0

class Triangulo(FiguraGeometrica):

    def __init__(self, base:float,altura:float, color_fondo , color_borde):
        print("Soy el constructor de Triangulo")
        super().__init__(color_fondo,color_borde) 
        self.base = base
        self.altura = altura
    
    def area(self) -> float :
        print("Soy el area del Triangulo")
        return ( self.base * self.altura ) / 2

    def perimetro(self) -> float:

        print("Soy el perimetro del triángulo")
        
        return 0


class Circulo(FiguraGeometrica):

    def __init__(self, radio:float, color:str):
        super().__init__(color)
        print("Soy el constructor de Circulo")
        self.radio = radio

    def area(self) -> float :
        print("Soy el area del circulo")

        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        print("Soy el perimetro del circulo")

        return math.pi * self.radio * 2 


def main():
    
    
    circulo1 = Circulo(5, "amarillo", "negro")
    print("El color de este circulo es ",circulo1.color_fondo)
    area = circulo1.area()
    print(f"El area de un circulo de {circulo1.radio:.2f} es {area:.2f}")
    perimetro = circulo1.perimetro()
    print(f"El perimetro de un circulo de {circulo1.radio:.2f} es {perimetro:.2f}")


    triangulo1 = Triangulo()
    triangulo1.area()
    print("El área de un triángulo de base {triangulo1.base:.2f} cm y altura {triangulo1.altura: .2f} cm es {t1.area}")
    triangulo1.perimetro()



main()

