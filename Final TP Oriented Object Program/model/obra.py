from model.tipo_obra import TipoObra
from model.etapa import Etapa
from model.area import Area
from model.barrio import Barrio
from model.empresa import Empresa
from model.tipo_contratacion import TipoContratacion
from model.fuente_financiamiento import FuenteFinanciamiento
from model.imagen import Imagen


class Obra():
    def __init__(self,entorno:str,nombre:str,etapa:Etapa, tipo_obra:TipoObra,area_responsable:Area,descripcion:str,monto_contrato:float,barrio:Barrio, direccion:str ,fecha_inicio="01/01/2000",fecha_fin_inicial="01/01/2000",plazo_meses:int= 0,porcentaje_avance:float = 0,empresa:Empresa = "",licitacion_anio:int= 0,tipo_contratacion:TipoContratacion = "",nro_contratacion:str= 0,beneficiarios:str= "",mano_obra:int=0,destacada:bool= True,expediente_numero:str=0,fuente_financiamiento:FuenteFinanciamiento="",imagenes:Imagen = []) -> None:
        
        self.entorno = entorno
        self.nombre= nombre
        self.etapa = etapa
        self.tipo_obra = tipo_obra
        self.area_responsable = area_responsable
        self.descripcion = descripcion
        self.monto_contrato = monto_contrato
        self.barrio = barrio
        self.direccion = direccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.plazo_meses = plazo_meses
        self.porcentaje_avance = porcentaje_avance
        self.imagenes = []
        self.empresa = empresa
        self.licitacion_anio = licitacion_anio
        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion
        self.beneficiarios = beneficiarios
        self.mano_obra = mano_obra
        self.destacada = destacada
        self.expediente_numero = expediente_numero
        self.fuente_financiamiento = fuente_financiamiento

    @property
    def entorno(self):
        return self.__entorno

    @entorno.setter
    def entorno(self,valor):
        self.__entorno = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def etapa(self):
        return self.__etapa
    
    @etapa.setter
    def etapa(self, valor):
        self.__etapa = valor

    @property
    def tipo_obra(self):
        return self.__tipo_obra
    
    @tipo_obra.setter
    def tipo_obra(self, valor):
        self.__tipo_obra = valor

    @property
    def area_responsable(self):
        return self.__area_responsable
    
    @area_responsable.setter
    def area_responsable(self, valor):
        self.__area_responsable = valor

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def monto_contrato(self):
        return self.__monto_contrato
    
    @monto_contrato.setter
    def monto_contrato(self, valor):
        self.__monto_contrato = valor

    @property
    def barrio(self):
        return self.__barrio
    
    @barrio.setter
    def barrio(self, valor):
        self.__barrio = valor

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self.__fecha_inicio = valor

    @property
    def fecha_fin_inicial(self):
        return self.__fecha_fin_inicial
    
    @fecha_fin_inicial.setter
    def fecha_fin_inicial(self, valor):
        self.__fecha_fin_inicial = valor

    @property
    def plazo_meses(self):
        return self.__plazo_meses
    
    @plazo_meses.setter
    def plazo_meses(self, valor):
        self.__plazo_meses = valor

    @property
    def porcentaje_avance(self):
        return self.__porcentaje_avance
    
    @porcentaje_avance.setter
    def porcentaje_avance(self, valor):
        self.__porcentaje_avance = valor

    @property
    def imagenes(self):
        return self.__imagenes
    
    @imagenes.setter
    def imagenes(self, valor):
        self.__imagenes = valor

    @property
    def empresa(self):
        return self.__empresa
    
    @empresa.setter
    def empresa(self, valor):
        self.__empresa = valor

    @property
    def licitacion_anio(self):
        return self.__licitacion_anio
    
    @licitacion_anio.setter
    def licitacion_anio(self, valor):
        self.__licitacion_anio = valor

    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion
    
    @tipo_contratacion.setter
    def tipo_contratacion(self, valor):
        self.__tipo_contratacion = valor

    @property
    def nro_contratacion(self):
        return self.__nro_contratacion
    
    @nro_contratacion.setter
    def nro_contratacion(self, valor):
        self.__nro_contratacion = valor

    @property
    def beneficiarios(self):
        return self.__beneficiarios
    
    @beneficiarios.setter
    def beneficiarios(self, valor):
        self.__beneficiarios = valor

    @property
    def mano_obra(self):
        return self.__mano_obra
    
    @mano_obra.setter
    def mano_obra(self, valor):
        self.__mano_obra = valor

    @property
    def destacada(self):
        return self.__destacada
    
    @destacada.setter
    def destacada(self, valor):
        self.__destacada = valor

    @property
    def expediente_numero(self):
        return self.__expediente_numero
    
    @expediente_numero.setter
    def expediente_numero(self, valor):
        self.__expediente_numero = valor

    @property
    def fuente_financiamiento(self):
        return self.__fuente_financiamiento
    
    @fuente_financiamiento.setter
    def fuente_financiamiento(self, valor):
        self.__fuente_financiamiento = valor



    def iniciar_contratacion(self,tipo:TipoContratacion,nro_contratacion:str):
        self.tipo_contratacion = tipo
        self.nro_contratacion = nro_contratacion


    def adjudicar_obra(self,empresa:Empresa,expediente_numero:str):
        self.empresa = empresa
        self.expediente_numero = expediente_numero
        
        

    def iniciar_obra(self,valor_destacada:bool,fechaInicio:str,fechaFinal:str,fuente_financiamiento:FuenteFinanciamiento,mano_obra:int):
        self.destacada = valor_destacada
        self.fecha_inicio = fechaInicio
        self.fecha_fin_inicial = fechaFinal
        self.fuente_financiamiento = fuente_financiamiento
        self.mano_obra = mano_obra
        print("------------------------------------------------Inicializacion de obra correcta !------------------------------------------------")
        

    def actualizar_porcentaje_avance(self,porc_incremento:int):
        self.porcentaje_avance = porc_incremento
        

    def incrementar_plazo(self,meses:int):
        self.plazo_meses = meses

    def agregar_imagenes(self,nombre:str):
        imagen = Imagen(f"{nombre}")
        self.imagenes.append(imagen)

    def incrementar_mano_obra(self,cantidad:int):
        self.mano_obra = cantidad

    def finalizar_obra(self):
        self.etapa = "Finalizada"
        self.actualizar_porcentaje_avance(100)


    def rescindir_obra(self):
        self.etapa = "Rescindida"