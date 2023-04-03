
numero = int(input("Ingrese numero: "))
#Punto A 

lista = []

while numero != 0: 
    lista.append(numero)
    numero = int(input("Ingrese numero: "))


print("Lista de numeros :", lista)


#Punto B

numero_a_eliminar = int(input("Ingrese numero a eliminar : "))
encontrado = False
for valor in lista:
    if valor == numero_a_eliminar:
        lista.remove(numero_a_eliminar)
        encontrado = True

if not encontrado:
   print("No se puede eliminar el número.")

#PuntoC
suma = 0
for valor in lista:
    suma = suma + valor

print("Suma de  los numeros en la lista:",suma)
#Punto D


lista_menores = []
for valor in lista:
    if valor < numero:
        lista_menores.append(valor)


print("Lista con valores menores: {}".format(lista_menores))


print("Nueva lista :",lista)