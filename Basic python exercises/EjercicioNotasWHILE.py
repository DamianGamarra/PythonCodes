condicion = True
print("Bienvenido al bucle")
i = 0
sumaTotal = 0



while (condicion):
    nota = int(input("Ingrese nota: "))

    while (nota <= 0 or nota > 10):
        nota = int(input("Error de nota. Ingrese nuevamente: "))

    sumaTotal = sumaTotal + nota  #acumulador
    i = i + 1 # contador o acumulador de a 1 
    opcion = input("Desea seguir ingresando datos : (si/no): ")

    if opcion == "no":
        condicion = False

promedio = float(sumaTotal) / i

print("El promedio es : {}".format(promedio))
print("Fin del programa")