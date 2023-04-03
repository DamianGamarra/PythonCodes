cantHabitCens = 0
totalHabitCens = 0
totalMenores = 0
joven = 100
viejo = 0
ingresosTotal = 0
totalVehiculos = 0
tieneVehiculo = 0

integrFamilia = int(input("Ingrese cantidad de integrantes en la familia: "))

while integrFamilia != 0 :

    menores = int(input("Ingrese cantidad de menores de edad en la familia: "))
    ingresoSalarial = float(input("Coloque el ingreso salarial de la familia: "))
    edadViejo = int(input("Ingrese edad del mayor en la familia: "))
    edadJoven = int(input("Ingrese edad del menor en la familia: "))
    vehiculo = str(input("¿Hay algún vehículo en la familia ? (s/n): "))

    if vehiculo == "s" :
        cantidadVehiculos = int(input("¿Cuántos vehículos tiene? :"))
        if cantidadVehiculos > 0 :
            totalVehiculos = totalVehiculos + cantidadVehiculos
    else : cantidadVehiculos = 0


    cantHabitCens = cantHabitCens + 1
    totalHabitCens = totalHabitCens + integrFamilia
    totalMenores = totalMenores + menores
    ingresosTotal = ingresosTotal + ingresoSalarial
    
    if edadJoven < joven :
        joven = edadJoven
    
    if edadViejo > viejo :
        viejo = edadViejo


    
    integrFamilia = int(input("Ingrese cantidad de integrantes en la familia: "))

print("La cantidad de habitantes censados es de : {}".format(cantHabitCens))

print("El promedio de habitantes por hogar censados es de {}".format(totalHabitCens/cantHabitCens))

print("El porcentaje de menores por hogar censados es de {}%".format(totalMenores/totalHabitCens*100))

print("La persona más joven tiene {} años y la más vieja {} años.".format(joven,viejo))

print("El promedio de ingreso salarial por hogares censados es de {}$".format(ingresosTotal/cantHabitCens))

print("La cantidad de vehículos censados es de : {}".format(totalVehiculos))

print("El porcentaje de vehiculos por hogar censados es de {}%".format(totalVehiculos/cantHabitCens*100))

print("Fin del programa.")                                                                                        

