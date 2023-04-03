from funcionesSegundoParcial import totalHabitantes, personas_solas, personas_solas_porcentaje, cantMenoresTotal,salarioBajo
from funcionesSegundoParcial import noVehiculo, promediom2, nombre_mas_largo, personaDiscapacidad, guardado

departamentosTotales = 0
censo = []
while True :
    try:
        integrFamilia = int(input("Ingrese cantidad de integrantes en la familia: \n"))

        if integrFamilia == 0:
            break

        nombre_jefe_a = str(input("Ingrese el nombre del jefe/a de la familia: \n"))
        nombre_jefe_a = nombre_jefe_a.upper()
        while not nombre_jefe_a.isalpha():
            print("Solo se permiten letras!")
            nombre_jefe_a = str(input("Ingrese el nombre del jefe/a de la familia: \n"))

        cantMenores = int(input("Ingrese cantidad de menores de edad en la familia: \n"))

        cantMayores = int(input("Ingrese cantidad de mayores de 65 años en la familia: \n"))

        edadViejo = int(input("Ingrese edad del mayor en la familia: \n"))

        edadJoven = int(input("Ingrese edad del menor en la familia: \n"))

        personasDiscapacidad = int(input("¿Cuantas personas discapacitadas hay en la vivienda?: \n"))

        ingresoSalarial = int(input("Coloque el ingreso salarial de la familia: \n"))

        vehiculos = int(input("¿Cuántos vehículos tiene?: \n"))

        departamento = str(input("¿Vive en departamento o casa?: \n"))
        departamento = departamento.lower()
        if departamento == "departamento":
            departamentosTotales = departamentosTotales + 1 
            m2_depto =  int(input("¿Cuántos metros cuadrados tiene el departamento ?: \n"))
        elif departamento == "casa":
            m2_depto = 0

        datos = {
            "integrFamilia" : "",
            "nombre_jefe_a" : "",
            "cantMenores" : "",
            "cantMayores" : "",
            "edadViejo" : "",
            "edadJoven" : "",
            "personasDiscapacidad": "",
            "ingresoSalarial" : "",
            "vehiculos" : "",
            "m2_depto" : ""
        }

        datos["integrFamilia"] = integrFamilia
        datos["nombre_jefe_a"] = nombre_jefe_a
        datos["cantMenores"] = cantMenores
        datos["cantMayores"] = cantMayores
        datos["edadViejo"] = edadViejo 
        datos["edadJoven"] = edadJoven
        datos["personasDiscapacidad"] = personasDiscapacidad
        datos["ingresoSalarial"] = ingresoSalarial
        datos["vehiculos"] = vehiculos
        datos["m2_depto"] = m2_depto

        censo.append(datos)

    except ValueError:
        print("Debe ingresar un numero entero!")
    except NameError:
        print("Debe ingresar solamente casa o departamento")


print(censo)

totalHabitantes(censo)
nombre_mas_largo(censo)
personas_solas(censo)
personas_solas_porcentaje(censo)
cantMenoresTotal(censo)
salarioBajo(censo)
noVehiculo(censo)
print("Cantidad de familias que viven en departamentos: ",departamentosTotales)
promediom2(censo)
personaDiscapacidad(censo)
guardado(censo)