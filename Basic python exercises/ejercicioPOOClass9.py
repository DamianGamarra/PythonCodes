from abc import ABC
class Persona(ABC):

    def __init__ (self, nombre:str, apellido:str, dni:int, domicilio:str, edad:int, sexo:str):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio= domicilio 
        self.edad = edad
        self.sexo = sexo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,value):
        self.__apellido = value
    

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,value):
        self.__dni = value

    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self,value):
        self.__domicilio = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,value):
        self.__edad = value


    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,value):
        self.__sexo = value


    

    



class Profesor(Persona):

    def __init__(self,nombre, apellido, dni, domicilio, edad, sexo, nroLegajo:int, antiguedad:int, carrera, materias):
        super().__init__(nombre, apellido, dni, domicilio, edad, sexo)
        self.nroLegajo = nroLegajo
        self.antiguedad = antiguedad
        self.carrera = carrera
        self.materias = materias

    @property
    def nroLegajo(self):
        return self.__nroLegajo

    @nroLegajo.setter
    def nroLegajo(self,value):
        self.__nroLegajo = value

    @property
    def antiguedad(self):
        return self.__antiguedad

    @antiguedad.setter
    def antiguedad(self,value):
        self.__antiguedad = value

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self,value):
        self.__carrera = value

    @property
    def nroLegajo(self):
        return self.__nroLegajo

    @nroLegajo.setter
    def nroLegajo(self,value):
        self.__nroLegajo = value

class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, domicilio, edad, sexo, nroMatricula, carrera, materiasAprobadas = [], materiasCursando = []):
        super().__init__(nombre, apellido, dni, domicilio, edad, sexo)
        self.nroMatricula = nroMatricula
        self.carrera = carrera
        self.materiasAprobadas = materiasAprobadas
        self.materiasCursando = materiasCursando

    @property
    def nroMatricula(self):
        return self.__nroMatricula

    @nroMatricula.setter
    def nroMatricula(self,value):
        self.__nroMatricula = value

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self,value):
        self.__carrera = value
    
    @property
    def materiasAprobadas(self):
        return self.__materiasAprobadas

    @materiasAprobadas.setter
    def materiasAprobadas(self,value,materiasAprobadas):
        self.__materiasAprobadas = value
        materiasAprobadas.append(self.__materiasAprobadas)
            



    @property
    def materiasCursando(self):
        return self.__materiasCursando

    @materiasCursando.setter
    def materiasCursando(self,value):
        self.__materiasCursando.append(value)
    
    def promedioDeNotas(materiasAprobadas):
        promedioNotas = 0
        for i in materiasAprobadas:
            promedioNotas = i / len(materiasAprobadas)
        return print(promedioNotas)
    

    def inscripcionAFinal():
        pass

    def rendirFinal ():
        pass




    def __str__(self):
        return  "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nDomicilio: " + self.domicilio + "\nDni: " + str(self.dni) + "\nEdad: " + str(self.edad) + "\nSexo: " + self.sexo + "\nNroMatricula: " + str(self.nroMatricula) + "\nCarrera: " + self.carrera

class Carrera():

    def __init__(self,codigo,nombre,tituloOtorgado) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.tituloOtorgado = tituloOtorgado

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,value):
        self.__codigo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def tituloOtorgado(self):
        return self.__tituloOtorgado

    @tituloOtorgado.setter
    def tituloOtorgado(self,value):
        self.__tituloOtorgado = value

class Materia(ABC):

    def __init__(self,codigo,nombre,carrera,modalidad):

        self.codigo = codigo
        self.nombre = nombre
        self.carrera = carrera 
        self.modalidad = modalidad

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,value):
        self.__codigo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self,value):
        self.__carrera = value
        
    @property
    def modalidad(self):
        return self.__modalidad

    @modalidad.setter
    def modalidad(self,value):
        self.__modalidad = value

    def __str__(self):
        return "Codigo: " + str(self.codigo) + "\nNombre de la materia: " + self.nombre + "\nCarrera: " + self.carrera + "\nModalidad: " + self.modalidad


class MateriaAprobada(Materia):

    def __init__(self,notaFinal, codigo, nombre, carrera, modalidad):

        super().__init__(codigo, nombre, carrera, modalidad)
        self.notaFinal = notaFinal

    @property
    def notaFinal(self):
        return self.__notaFinal

    @notaFinal.setter
    def notaFinal(self,value):
        self.__notaFinal = value

    def __str__(self):
        return super().__str__() + "\nnotaFinal: " + str(self.notaFinal) 
        

class MateriaCursando(Materia):

    def __init__(self, notaParcial,asistencia,codigo, nombre, carrera, modalidad):

        super().__init__(codigo, nombre, carrera, modalidad)
        self.notaParcial = notaParcial
        self.asistencia = asistencia

    @property
    def notaParcial(self):
        return self.__notaParcial

    @notaParcial.setter
    def notaParcial(self,value):
        self.__notaParcial = value    

    @property
    def asistencia(self):
        return self.__asistencia

    @asistencia.setter
    def asistencia(self,value):
        self.__asistencia = value

def main():

    alumno1 = Alumno("Damián","Gamarra",41837308,"Av Corrientes 4500", 23,"M",254785,"TSDS")
    print(alumno1)

    materia1 = MateriaAprobada(9,3232,"Algebra","TSDS","virtual")

    materia2 = MateriaAprobada(7,3231,"POO","TSDS","virtual")
    print(materia1)
    print(materia2)

    




main()
