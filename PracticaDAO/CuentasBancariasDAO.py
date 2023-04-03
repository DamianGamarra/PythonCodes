from abc import ABC, abstractmethod 
import sqlite3

class DAO(ABC):
    @abstractmethod
    def conectar_bd(self):
        pass

    @abstractmethod
    def crear_tabla(self):
        pass

    @abstractmethod
    def insertar_registro(self, objeto):
        pass

    @abstractmethod
    def seleccionar_registro(self, objeto):
        pass

    @abstractmethod
    def seleccionar_todos_registros(self):
        pass

    @abstractmethod
    def eliminar_registro(self, objeto):
        pass

    @abstractmethod
    def modificar_registro(self, objeto, valores):
        pass

#Clase concreta que implementa la interface Data Access Object
class Cliente_DAO(DAO):
    def __init__(self) -> None:
        self.nombre_bd = "cuentas_bancarias.db"
        self.nombre_tabla = "clientes"
    
    @property
    def nombre_bd(self):
        return self.__nombre_bd
    
    @nombre_bd.setter
    def nombre_bd(self, valor):
        self.__nombre_bd = valor
    
    @property
    def nombre_tabla(self):
        return self.__nombre_tabla
    
    @nombre_tabla.setter
    def nombre_tabla(self, valor):
        self.__nombre_tabla = valor

    def conectar_bd(self):
        try:
            db = sqlite3.connect("clase12/" + self.nombre_bd)
            #print("La conexion a la bd se ha realizado correctamente")
            return db, db.cursor()
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
            return None
    
    def crear_tabla(self):
        try:
            db, cursor = self.conectar_bd()
            # Crear una tabla
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.nombre_tabla} (
                "id"	INTEGER NOT NULL,
                "razon_social"	TEXT NOT NULL,
                "cuit"	TEXT NOT NULL,
                "domicilio"	TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );''')
            print("La tabla se ha creado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
        finally:
            db.close()
    
    def insertar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla} (razon_social,cuit,domicilio)
                VALUES
                ('{objeto.razon_social}', '{objeto.CUIT}', '{objeto.domicilio}');'''
            )
            # Guardar (commit) los cambios
            db.commit()
            print("El registro se ha insertado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al insertar un registro. {e}")
        finally:
            db.close()
    
    def insertar_varios_registros(self, lista):
        try:
            db, cursor = self.conectar_bd()
            lista_clientes = []
            for cliente in lista:
                cliente_tupla = (cliente.razon_social, cliente.CUIT, cliente.domicilio)
                lista_clientes.append(cliente_tupla)
            # Insertar los registros a la tabla
            cursor.executemany(f'''INSERT INTO {self.nombre_tabla} (razon_social,cuit,domicilio)
                VALUES (?,?,?)''', lista_clientes)
            # Guardar (commit) los cambios
            db.commit()
            print("Los registros se han insertado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al insertar los registros. {e}")
        finally:
            db.close()
    
    def seleccionar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE cuit='{objeto.CUIT}'")
            print(cursor.fetchone())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar el registro correspondiente al cuit={objeto.CUIT}. {e}")
        finally:
            db.close()
    
    def seleccionar_todos_registros(self):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla}")
            print(cursor.fetchall())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar todos los registros. {e}")
        finally:
            db.close()
    
    def eliminar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"DELETE FROM {self.nombre_tabla} WHERE cuit='{objeto.CUIT}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El registro correspondiente al cuit {objeto.CUIT} se ha eliminado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el registro correspondiente al cuit {objeto.CUIT}. {e}")
        finally:
            db.close()

    def modificar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"UPDATE {self.nombre_tabla} SET domicilio='{objeto.domicilio}' WHERE cuit='{objeto.CUIT}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El domicilio correspondiente al cuit {objeto.CUIT} se ha actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al modificar el domicilio correspondiente al cuit {objeto.CUIT}. {e}")
        finally:
            db.close()
    
    def obtener_registros(self):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla}")
            return cursor.fetchall()
        except Exception:
            return None
        finally:
            db.close()

#Clase abstracta que hereda la interface Data Access Object
class CuentaBancaria_DAO(DAO, ABC):
    def __init__(self, nombre_tabla) -> None:
        self.nombre_bd = "cuentas_bancarias.db"
        self.nombre_tabla = nombre_tabla
    
    @property
    def nombre_bd(self):
        return self.__nombre_bd
    
    @nombre_bd.setter
    def nombre_bd(self, valor):
        self.__nombre_bd = valor
    
    @property
    def nombre_tabla(self):
        return self.__nombre_tabla
    
    @nombre_tabla.setter
    def nombre_tabla(self, valor):
        self.__nombre_tabla = valor

    @abstractmethod
    def conectar_bd(self):
        pass

    @abstractmethod
    def crear_tabla(self):
        pass

    @abstractmethod
    def insertar_registro(self, objeto):
        pass

    @abstractmethod
    def seleccionar_registro(self, objeto):
        pass

    @abstractmethod
    def seleccionar_todos_registros(self):
        pass

    @abstractmethod
    def eliminar_registro(self, objeto):
        pass

    @abstractmethod
    def modificar_registro(self, objeto, valores):
        pass

#Clase concreta que hereda de CuentaBancaria_DAO
class CajaAhorro_DAO(CuentaBancaria_DAO):
    def __init__(self) -> None:
        super().__init__("caja_de_ahorro")

    def conectar_bd(self):
        try:
            db = sqlite3.connect("clase12/" + self.nombre_bd)
            #print("La conexion a la bd se ha realizado correctamente")
            return db, db.cursor()
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
            return None
    
    def crear_tabla(self):
        try:
            db, cursor = self.conectar_bd()
            # Crear una tabla
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.nombre_tabla} (
                "id"	INTEGER NOT NULL,
                "cuit_cliente"	TEXT NOT NULL,
                "nro_cuenta"	TEXT NOT NULL,
                "saldo"	REAL NOT NULL,
                "limite_extracciones"	INTEGER NOT NULL,
                "cant_extracciones"	INTEGER NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );''')
            print("La tabla se ha creado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
        finally:
            db.close()
    
    def insertar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla}
                (cuit_cliente,nro_cuenta,saldo,limite_extracciones,cant_extracciones)
                VALUES
                ('{objeto.titular.CUIT}', '{objeto.nro_cuenta}', {objeto.saldo}, {objeto.limite_extracciones}, {objeto.cant_extracciones});'''
            )
            # Guardar (commit) los cambios
            db.commit()
            print("El registro se ha insertado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al insertar un registro. {e}")
        finally:
            db.close()
    
    def seleccionar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE nro_cuenta='{objeto.nro_cuenta}'")
            print(cursor.fetchone())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar el registro correspondiente al cuit={objeto.CUIT}. {e}")
        finally:
            db.close()
    
    def insertar_varios_registros(self, lista):
        db, cursor = self.conectar_bd()
        cursor.execute(f"")

    def seleccionar_todos_registros(self):
        pass
    
    def eliminar_registro(self, objeto):
        pass

    def modificar_registro(self, objeto):
        pass
    
    def obtener_registros(self):
        pass

#Clase concreta que hereda de CuentaBancaria_DAO
class CuentaCorriente_DAO(CuentaBancaria_DAO):
    pass