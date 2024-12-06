import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'calculadora'
            )
            if self.conn.is_connected():
                print("Conexión exitosa a la base de datos")
            
        except Error as e:  
            print(f"Error al conectar la base de datos: {e}")
            
            
                        
    def Close_conection(self):
        if self.conn.is_connected():
            self.conn.close()
            print("Conexión cerrada")
            
if __name__ == "__main__":
    db = DatabaseConnection()
    db.Close_conection()