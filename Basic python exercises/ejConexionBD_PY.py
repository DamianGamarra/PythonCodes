import sqlite3

def open_conection_db():
    bd = sqlite3.connect("Empelados.bd")
    print("Base de datos abierta")
    return bd

def crear_tabla():
    cursor.execute('''CREATE TABLE IF NOT EXIST  "empleados" (
    "id" INTEGER NOT NULL,
    "numero_legajo" INTEGER NOT NULL UNIQUE,
    "dni" INTEGER NOT NULL UNIQUE,
    "nombre_empleado" TEXT NOT NULL,
    "apellido_empleado" TEXT NOT NULL
    "area" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT));''')


def insertar_nuevo_registro(bd,cursor,valores):

    cursor.execute("INSERT INTO empleados VALUES (?,?,?,?,?)",valores)
    bd.commit()
    bd.close()

def seleccion_un_registro(cursor,dni):

    cursor.execute('SELECT * FROM empleados WHERE dni=?',[dni])
    print(cursor.fetchone())


open_conection_db()
cursor = bd.cursor()
crear_tabla()



print("Ingrese la opción que desea ejecutar."
        "Opción 1: Insertar un registro de empleado"
        "Opción 2: Seleccionar un registro de empleado a partir de su número de DNI"
        "Opción 3: Seleccionar todos los empleados o los registros de la tabla."
        "Opción 4: Modificar el area de un empleado en función de su numero de legajo."
        "Opción 5: Eliminar un empleado a partir del numero de legajo."
        "Opción 6: Finalizar")

    opcion = input("Ingrese la opción que desea ejecutar:")
    if opcion == "1":
        insertar_nuevo_registro()
    if opcion == "2":
        seleccion_un_registro(input("Ingrese un DNI: "))