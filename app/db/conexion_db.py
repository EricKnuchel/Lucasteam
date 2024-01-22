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
            return conn

    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")
        return None

def create_table():
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            
            command = """
            CREATE TABLE IF NOT EXISTS Juegos(
                id INT AUTO_INCREMENT Primary key,
                nombre Varchar(255) NOT NULL,
                plataforma Varchar(255),
                year INT(4) NOT NULL,
                genero Varchar(255),
                publisher VARCHAR(255),
                V_NA Double ,
                V_EU Double ,
                V_JP Double ,
                V_other Double ,
                V_Global Double
            )
            """
            cursor.execute(command)
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
            