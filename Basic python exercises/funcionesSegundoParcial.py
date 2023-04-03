import csv 

def totalHabitantes(censo):
    
    habitantesTotales = 0

    for item in censo :
        habitantesTotales = habitantesTotales + item["integrFamilia"]

    print("La cantidad de habitantes censados es de : ",habitantesTotales)
    
    return



def personas_solas(censo):
    cont = 0
    for item in censo:

        if item["integrFamilia"] == 1 :
            cont = cont + item["integrFamilia"]
    
    print("Cantidad de personas que viven solas: ",cont)

    return
        


def personas_solas_porcentaje(censo):
    
    acum = 0
    contPersonas_solas = 0
    for item in censo:
        acum = acum + 1
        if item["integrFamilia"] == 1 :
            contPersonas_solas = contPersonas_solas + 1

    print('El porcentaje de viviendas donde viven personas solas es: {}%'.format(contPersonas_solas/acum*100))
    
    return



def cantMenoresTotal(censo):

    cant_menores_total = 0
    for item in censo:

        if item["cantMenores"] > 0:
            cant_menores_total = cant_menores_total + item["cantMenores"]

    print("La cantidad de menores de 18 años registrados en el censo es de : ",cant_menores_total)

    return


def salarioBajo(censo):
    
    
    salario_mas_bajo = min(censo, key=lambda x:x['ingresoSalarial'])
            
    print("El salario familiar más bajo registrado es de : ",salario_mas_bajo["ingresoSalarial"])

    return


def noVehiculo(censo):

    cont = 0
    for item in censo:

        if item["vehiculos"] == 0 :
            cont = cont + 1
    
    print("Cantidad de familias que no poseen vehículo: ",cont)

    return



def promediom2(censo):

    acum = 0
    cont = 0
    for item in censo:
        if item["m2_depto"] > 0:
            acum = acum + item["m2_depto"]
        
            cont = cont + 1

    print("El promedio de metros cuadrados totales de departamentos es de : {}".format(acum/cont))

    return


def nombre_mas_largo(censo):
    
    nombre = "nombre_jefe_a"
    nombreLargo = [item[nombre] for item in censo]
    nombreLargo.sort(key=len)
    nombreLargo.reverse()


    print("El nombre con más caracteres de jefe/a es : ",nombreLargo[0])
    
    return


def personaDiscapacidad(censo):

    acum = 0
    cont = 0
    for item in censo:
        cont = cont + 1
        if item["personasDiscapacidad"] > 0:
            acum = acum + item["personasDiscapacidad"]
        
    print("El porcentaje de personas discapacitadas por vivienda es de : {}%".format(acum/cont*100))

    return



def guardado(censo):

    titulos = ["integrFamilia", "nombre_jefe_a", "cantMenores", "cantMayores", "edadViejo", "edadJoven", "personasDiscapacidad", "ingresoSalarial", "vehiculos", "m2_depto"]

    with open("censo.csv", "w") as file :

        escribir = csv.DictWriter(file, fieldnames=titulos)

        escribir.writeheader()
        escribir.writerows(censo)

    return

