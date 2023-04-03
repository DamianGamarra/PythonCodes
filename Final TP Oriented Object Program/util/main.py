from abc import ABC
from util.gestionar_dao import GestionarDAO
from util.gestionar_modelo import GestionarModelo
from model.obra import Obra
class Main(ABC):
    
    @classmethod
    def main(cls):
        #importar dataset .csv a la base de datos
        archivo_csv = "./observatorio-de-obras-urbanas.csv"
        #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-general-y-relaciones-internacionales/ba-obras/observatorio-de-obras-urbanas.csv"
        GestionarDAO.importar_csv(archivo_csv)

        #agregar aquí su código para completar las funcionalidades del TP

        contador = 0
        while contador < 3:

            #PUNTO 3A
            obj_etapa_dao = GestionarDAO.crear_objeto_dao("Etapa_DAO")
            id_etapa = 0            
            for i in obj_etapa_dao.obtener_registros():
                if (i[1] == "Proyecto"):
                    id_etapa = int(i[0])
                    obj_etapa = GestionarModelo.nueva_etapa(i[1])
                    break
            if id_etapa == 0:
                obj_etapa = GestionarModelo.nueva_etapa("Proyecto")
                print("La etapa de la obra fue inicializada en:Proyecto")
                GestionarDAO.insertar_registro(obj_etapa_dao,obj_etapa)


            #PUNTO 4B(CREACION DE LOS OBJETOS QUE SON SOLICITADOS COMO PARAMETROS PARA INICIAR LA OBRA Y PEDIDA DE PARAMETROS POR CONSOLA PARA QUE LUEGO DE UNA MANERA AUTOMATIZADA LOS ATRIBUTOS DE LAS INSTANCIAS  OBRA, TOMEN ESOS VALORES)
            obj_tipo_obra_dao = GestionarDAO.crear_objeto_dao("TipoObra_DAO")
            while True:
                descrip_tipo_obra = input("Escriba el tipo de obra(Arquitectura/Vivienda/Escuelas/Hidráulica E Infraestructura/ Salud/Espacio Público/ Hidráulica e Infraestructura/Transporte/Vivienda Nueva/Infraestructura): ")
                id_tipo_obra = 0
                for i in obj_tipo_obra_dao.obtener_registros():
                    if (i[1] == descrip_tipo_obra) :
                        id_tipo_obra = int(i[0])
                        break
                if id_tipo_obra > 0:
                    obj_tipo_obra = GestionarModelo.nuevo_tipo_obra(descrip_tipo_obra)
                    print("El tipo de obra fue ingresado correctamente.")
                    break
                else:
                    print("-----------El tipo de obra ingresado no existe en la BD-----------")


            obj_area_responsable_dao = GestionarDAO.crear_objeto_dao("Area_DAO")
            while True:
                descrip_area_responsable = input("Ingrese el tipo de área (Ministerio de Espacio Público e Higiene Urbana/Subsecretaría de Gestión Comunal/Corporación Buenos Aires Sur/Ministerio de Educación/Secretaría de Transporte y Obras Públicas/Ministerio de Salud/Ministerio de Desarrollo Humano y Hábitat/Instituto de la Vivienda/Ministerio de Cultura/Ministerio de Justicia y Seguridad) :")
                id_area_responsable = 0
                for i in obj_area_responsable_dao.obtener_registros():
                    if (i[1] == descrip_area_responsable) :
                        id_area_responsable = int(i[0])
                        break
                if id_area_responsable > 0:
                    obj_area_responsable = GestionarModelo.nueva_area(descrip_area_responsable)
                    print("El tipo de área fue ingresado correctamente.")
                    break
                else:
                    print("-----------El tipo de área ingresado no existe en la BD-----------")


            obj_comuna_dao= GestionarDAO.crear_objeto_dao("Comuna_DAO")
            while True:
                numero_comuna = input("-----------Ingrese el numero de comuna : -----------")
                id_comuna = 0
                for i in obj_comuna_dao.obtener_registros():
                    if (i[0] == numero_comuna) :
                        id_comuna = int(i[0])
                        break
                if id_comuna == 0:
                    obj_comuna = GestionarModelo.nueva_comuna(numero_comuna)
                    break
                else:
                    print("El número de comuna ingresado no existe en la BD")



            obj_barrio_dao = GestionarDAO.crear_objeto_dao("Barrio_DAO")
            while True:
                descrip_barrio = input("-----------Ingrese el nombre del barrio: -----------")
                id_barrio = 0
                for i in obj_barrio_dao.obtener_registros():
                    if (i[1] == descrip_barrio) :
                        id_barrio = int(i[0])
                        break
                if id_barrio > 0:
                    obj_barrio = GestionarModelo.nuevo_barrio(descrip_barrio,obj_comuna)
                    break
                else:
                    print("-----------El nombre del Barrio ingresado no existe en la BD-----------")


            nuevo_entorno = input("-----------Ingrese el nombre del nuevo entorno: -----------")
            nuevo_nombre = input("-----------Ingrese el nuevo nombre de la obra: -----------")
            nueva_descripcion = input("-----------Ingrese la descripcion  de la nueva obra: -----------")
            nuevo_monto_contrato = input("-----------Ingresar el monto del contrato: -----------")
            nueva_direccion = input("-----------Ingrese una direccion: -----------")
            nuevo_plazo_meses = input("-----------Ingrese el plazo de meses: -----------")
            nuevo_beneficiarios = input("-----------Ingrese el nombre de los beneficiarios: -----------")

            obj_obra = GestionarModelo.nueva_obra(nuevo_entorno,nuevo_nombre,obj_etapa,obj_tipo_obra,obj_area_responsable,nueva_descripcion,nuevo_monto_contrato,obj_barrio,nueva_direccion,nuevo_plazo_meses,nuevo_beneficiarios)
            
            descrip_tipo_contratacion = input(-----------"Escriba el nuevo tipo de contratacion: -----------")
            obj_tipo_contratacion,id_tipo_contratacion = GestionarModelo.nuevo_tipo_contratacion(descrip_tipo_contratacion)
            
            cuit = input("-----------Ingrese el cuit de la empresa: -----------")
            razon_social =input("-----------Ingresar la razon social de la empresa: -----------")
            obj_empresa,id_empresa = GestionarModelo.nueva_empresa(cuit,razon_social)

            descrip_fuente_financiamiento =input("Ingrese la fuente de financiamiento: ")
            obj_fuente_financiamiento, id_fuente_financiamiento = GestionarModelo.nueva_fuente_financiamiento(descrip_fuente_financiamiento)

            nro_contratacion=input("-----------Ingrese un numero de contratacion: -----------")
            Obra.iniciar_contratacion(obj_obra,obj_tipo_contratacion,nro_contratacion)

            expediente_numero = input("-----------Ingrese un numero de expediente: -----------")
            Obra.adjudicar_obra(obj_obra,obj_empresa,expediente_numero)
            print("------------------------------------------------")
            fecha_Inicio = input("Ingrese la fecha de inicio: ")
            print("------------------------------------------------")
            fecha_Final = input("Ingrese la fecha del final de la obra: ")
            print("------------------------------------------------")
            mano_obra = input("Ingrese la cantidad de mano de obra: ")
            print("------------------------------------------------")
            valor_destacada = input("Ingrese si la obra es destacada o no escribiendo True o False:")
            print("------------------------------------------------")
            Obra.iniciar_obra(obj_obra,valor_destacada,fecha_Inicio,fecha_Final,obj_fuente_financiamiento,mano_obra)
            

            obj_obra_dao = GestionarDAO.crear_objeto_dao("Obra_DAO")
            lista_ids = (id_etapa,id_tipo_obra,id_area_responsable,id_barrio,id_tipo_contratacion,id_empresa,id_fuente_financiamiento)

            #PERSISTENCIA DE LAS DISTINTAS INSTANCIAS DE OBRA
            if contador == 0:
                obj1_obra = obj_obra
                print("------------------------Se guardo el objeto 1 ------------------------")
            
            if contador == 1:
                obj2_obra = obj_obra
                print("------------------------Se guardo el objeto 2 ------------------------")
            if contador ==2:
                obj3_obra = obj_obra
                print("------------------------Se guardo el objeto 3 ------------------------")



            contador = contador + 1






        #PUNTO 5 AL 13, CAMBIOS EN LA INSTANCIA DE OBRA (SÓLO HARCODEAMOS EL CAMBIO EN LA INSTANCIA DE OBRA 2)
        porcentaje_avance = input("-----------Ingrese el nuevo porcentaje de la instancia de obra 2(Objeto2): -----------")
        Obra.actualizar_porcentaje_avance(obj2_obra,porcentaje_avance)
        print(f"Se ha actualizado correctamente el porcentaje de avance, es : {obj2_obra.porcentaje_avance}")

        plazo_meses = input("-----------Ingrese el nuevo incremento de plazo de meses de la instancia de obra 2(Objeto2): -----------")
        Obra.incrementar_plazo(obj2_obra,plazo_meses)
        print("Se ha incrementado correctamente el plazo de meses")

        imagen_nueva = input("-----------Ingrese el nombre de la nueva imagen de la instancia de obra 2(Objeto2): -----------")
        Obra.agregar_imagenes(obj2_obra,imagen_nueva)

        mano_obra_incrementada = input("-----------Ingrese la cantidad de mano de obra que quiere aumentar de la instancia de obra 2(Objeto2): -----------")
        Obra.incrementar_mano_obra(obj2_obra,mano_obra_incrementada)


        print("-----------Finalización de la instancia de obra 2(Objeto2)-----------")
        Obra.finalizar_obra(obj2_obra)
        print("-----------La etapa de la obra fue actualizada a finalizada.-----------")

        print("-----------Rescindiendo la instancia de la obra 1(Objeto1)-----------")
        Obra.rescindir_obra(obj1_obra)

        #PUNTO 14, SI LA OBRA SE ENCUENTRA FINALIZADA O RESCINDIDA SE AGREGARAN A LA BASE DE DATOS(FINALIZAMOS LA INSTANCIA 2 Y RESCINDIMOS LA INSTANCIA 1,ESAS 2 SERÁN AGREGADAS A LA BASE DE DATOS Y LA INSTANCIA 3 ES LA QUE NO VA A SER AGREGADA YA QUE NO SE ENCUENTRA FINALIZADA O RESCINDIDA)
        print("-----------A continuación se ingresaran en la base de datos sólo la instancia de obra 1 y 2 (Rescindida y Finalizada)-----------")
        if obj1_obra.etapa == "Finalizada" or obj1_obra.etapa == "Rescindida":
            GestionarDAO.insertar_registro(obj_obra_dao,obj1_obra,lista_ids)

        if obj2_obra.etapa == "Finalizada" or obj2_obra.etapa == "Rescindida":
            GestionarDAO.insertar_registro(obj_obra_dao,obj2_obra,lista_ids)

        if obj3_obra.etapa == "Finalizada" or obj3_obra.etapa == "Rescindida":
            GestionarDAO.insertar_registro(obj_obra_dao,obj3_obra,lista_ids)









        #PUNTO 15: MOSTRAMOS EN CONSOLA LOS VALORES PEDIDOS DE LA BASE DE DATOS A TRAVES DE QUERYS SQL (MÉTODOS EN OBRA_DAO.PY)

        print("------------------------Los tipos de area son: ------------------------")
        obj_obra_dao.obtener_registros_descripcion(obj_area_responsable_dao)
        print("\n")
        print("------------------------Los tipos de obra son : ------------------------")
        obj_obra_dao.obtener_registros_descripcion(obj_tipo_obra_dao)
        print("\n")
        print("------------------------Cantidad de obras por etapa en orden(Etapa:Cantidad):------------------------")
        obj_obra_dao.cantidad_obras_por_etapa()




        print("\n")
        print("------------------------Cantidad de obras por tipo de obra en orden(Tipo de Obra de la 1 a la 10):------------------------")
        obj_obra_dao.cantidad_obras_por_tipo_obra()

        print("\n")
        print("------------------------Lista de todos los barrios pertenecientes a la comuna 1,2 y 3: ------------------------")
        obj_obra_dao.barrios_comuna_1_2_3(obj_barrio_dao)

        print("\n")
        print("------------------------Cantidad de obras finalizadas en la comuna 1: ------------------------")
        obj_obra_dao.cant_obras_finalizadas_com1(obj_barrio_dao)
        print("\n")
        print("------------------------Cantidad de obras finalizadas en un plazo menor o igual a 24 meses:------------------------")
        obj_obra_dao.obras_finalizadas_menos_o_igual_24meses()