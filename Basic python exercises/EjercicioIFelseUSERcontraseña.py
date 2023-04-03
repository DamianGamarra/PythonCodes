print("Bienvenido")
user = "dami"
passw = "12345"
condicion = True
error = 0
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

while(condicion):
    if usuario == user:
        if contraseña == passw:
            print("ingreso correcto!") 
            break
        else:
            print("Error de usuario/contraseña")
            error = error + 1

    else:
        print("Usuario incorrecto")
        error = error + 1

    if error == 3:
        condicion = False
    
    else: 
        usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

if error == 3:
    print("Usuario bloqueado")
else:
    print("Fin del bucle por usuario correcto")

print("Fin del programa")


