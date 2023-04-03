class Persona:
    def __init__(self,nombre,edad,dni):
        self.edad = edad
        self.nombre = nombre
        self.dni = dni


    def mostrar_edad(self) -> int :
        if self.edad >= 0:
            print("La edad de esta persona es :",self.edad)
        

    def es_mayor_edad(self) -> bool:
        if self.edad >= 18:
            print(True)

        else:
            return print(False)

PS = Persona("damian",23, 41837308)

PS.mostrar_edad()

PS.es_mayor_edad()

