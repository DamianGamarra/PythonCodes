from abc import ABC
from model.etapa import Etapa
from model.obra import Obra
from model.tipo_obra import TipoObra
from model.area import Area
from model.imagen import Imagen
from model.comuna import Comuna
from model.barrio import Barrio
from model.tipo_contratacion import TipoContratacion
from model.empresa import Empresa
from model.fuente_financiamiento import FuenteFinanciamiento
from util.gestionar_dao import GestionarDAO

class GestionarModelo(ABC):
    __listado_obras = []
    __listado_etapas = []
    __listado_tipos_obras = []
    __listado_areas = []
    __listado_comunas = []
    __listado_barrios = []
    __listado_tipos_contratacion = []
    __listado_empresas = []
    __listado_fuentes_financiamiento = []
    
    @classmethod
    def nueva_etapa(cls,nombre:str) -> Etapa:
        obj_etapa = Etapa(nombre)
        cls.__listado_etapas.append(obj_etapa)
        return obj_etapa

    @classmethod
    def nueva_obra(cls,entorno:str,nombre:str,etapa:Etapa,tipo_obra:TipoObra,area_responsable:Area,descripcion:str,monto_contrato:float,barrio:Barrio,direccion:str,plazo_meses:int,beneficiarios:str) -> Obra:
        
        obj_nueva_obra = Obra(entorno,nombre,etapa,tipo_obra,area_responsable,descripcion,monto_contrato,barrio,direccion,plazo_meses,beneficiarios)
        cls.__listado_obras.append(obj_nueva_obra)
        return obj_nueva_obra

    @classmethod
    def nuevo_tipo_obra(cls,descrip:str) -> TipoObra:
        obj_tipo_obra = TipoObra(descrip)
        
        cls.__listado_tipos_obras.append(obj_tipo_obra)
        return obj_tipo_obra

    @classmethod
    def nueva_area(cls,descrip:str) -> Area:
        obj_area = Area(descrip)
        cls.__listado_areas.append(obj_area)
        return obj_area
    
    @classmethod
    def nueva_comuna(cls,numero:int) -> Comuna:
        obj_comuna = Comuna(numero)
        cls.__listado_comunas.append(obj_comuna)
        return obj_comuna

    @classmethod
    def nuevo_barrio(cls,nombre:str,comuna:Comuna) -> Barrio:
        obj_barrio = Barrio(nombre,comuna)
        cls.__listado_barrios.append(obj_barrio)
        return obj_barrio

    @classmethod
    def nuevo_tipo_contratacion(cls,descrip:str) -> TipoContratacion:
        obj_tipo_contratacion_dao = GestionarDAO.crear_objeto_dao("TipoContratacion_DAO")
        while True:
            id_tipo_contratacion = 0
            for i in obj_tipo_contratacion_dao.obtener_registros():
                if (i[1] == descrip) :
                    id_tipo_contratacion = int(i[0])
                    break
            if id_tipo_contratacion > 0:
                obj_tipo_contratacion = TipoContratacion(descrip)
                break
            else:
                print("El nombre del tipo de contratacion ingresado no existe en la BD")
                break
        cls.__listado_tipos_contratacion.append(obj_tipo_contratacion)
        return obj_tipo_contratacion ,id_tipo_contratacion

    @classmethod
    def nueva_empresa(cls,cuit:int,razon_social:int) -> Empresa:        
        obj_empresa_dao = GestionarDAO.crear_objeto_dao("Empresa_DAO")
        id_empresa = 0            
        for i in obj_empresa_dao.obtener_registros():
            if (i[1] == cuit):
                id_empresa = int(i[0])
                obj_empresa = Empresa(cuit,razon_social)
                break
        if id_empresa == 0:
            obj_empresa = Empresa(cuit,razon_social)
            print(f"La nueva empresa de la obra es :{obj_empresa}")


        cls.__listado_empresas.append(obj_empresa)
        return obj_empresa , id_empresa
    
    @classmethod
    def nueva_fuente_financiamiento(cls,descrip) -> FuenteFinanciamiento:
        obj_fuenteFinanciamiento_dao = GestionarDAO.crear_objeto_dao("FuenteFinanciamiento_DAO")
        while True:
            id_fuente_financiamiento = 0
            for i in obj_fuenteFinanciamiento_dao.obtener_registros():
                if (i[1] == descrip) :
                    id_fuente_financiamiento = int(i[0])
                    break
            if id_fuente_financiamiento > 0:
                obj_fuenteFinanciamiento = FuenteFinanciamiento(descrip)
                break
            else:
                print("El nombre de la fuente de financiamiento ingresado no existe en la BD")
        
        cls.__listado_fuentes_financiamiento.append(obj_fuenteFinanciamiento)
        return obj_fuenteFinanciamiento , id_fuente_financiamiento
