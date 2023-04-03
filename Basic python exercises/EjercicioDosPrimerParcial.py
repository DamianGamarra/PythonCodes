lista_1 = []
print("Bienvenido al programa, a continuación ingrese 5 palabras.")

while len(lista_1) < 5:
    palabrasIngresadas = str(input("Ingrese una palabra: "))
    if len(palabrasIngresadas) > 20 or len(palabrasIngresadas) < 5 :
        print("ERROR. La palabra debe tener entre 5 y 20 caracteres.")
    else :
        lista_1.append(palabrasIngresadas)


lista_1.sort(key=len)

print(lista_1)