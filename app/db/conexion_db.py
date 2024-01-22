import mysql.connector
# import pymysql

def conectar_a_mysql():
    try:
        # Crear una conexión
        conn = mysql.connector.connect(            
            user = 'root',
            password = 'aeCB243cFb1aeagHf5cgecHDB35a3haB',
            host = 'viaduct.proxy.rlwy.net',
            database = 'railway',
            port = '52288'
            )

        if conn.is_connected():
            print("Conexión exitosa")
            return conn

    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")
        return None

def create_table():
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            
            cursor.execute("Drop table Juegos")
            
            command = """
            CREATE TABLE IF NOT EXISTS Juegos(
                id INT AUTO_INCREMENT Primary key,
                nombre Varchar(255) NOT NULL,
                plataforma Varchar(255),
                year INT(4) NOT NULL,
                genero Varchar(255),
                publisher VARCHAR(255),
                V_NA Double NOT NULL,
                V_EU Double NOT NULL,
                V_JP Double Not NULL,
                V_other Double NOT NULL,
                V_Global Double NOT NULL
            )
            """
            cursor.execute(command)
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
            