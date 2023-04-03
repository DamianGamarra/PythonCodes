print("Bienvenido al programa")

lado1 = float(input("La medida de a= "))
lado2 = float(input("La medida de b= "))
lado3 = float(input("La medida de c= "))

if (lado1 == lado2 == lado3) and lado1 !=0 and lado2 != 0 and lado3 != 0:
    print("Su triángulo es equilatero")
elif lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("ERROR. Digite numeros positivos")
else :
    if (lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado1 != lado2) or (lado1 == lado3 and lado2 != lado3):
        print("Su triángulo es isósceles")
    else: 
        print("Su triángulo es escaleno")


print("FIN DEL PROGRAMA.")
