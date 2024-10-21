import sqlite3

database = "tienda_juguetes.db"

class Database:
    def ejecutar_consulta(self, consulta, parametros = ()):
        # Método para ejecutar consultas SQL, admite parámetros opcionales
        # Se conecta a la base de datos utilizando SQLite y se ejecuta la consulta
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()  # Se obtiene el cursor para interactuar con la base de datos
            result = self.cursor.execute(consulta, parametros)  # Se ejecuta la consulta con los parámetros proporcionados
            conn.commit()  # Se guardan los cambios realizados en la base de datos
            return result  # Se devuelve el resultado de la consulta
        

# db = Database()

# resultado = db.ejecutar_consulta("Select * from producto")
# print(resultado.fetchall())