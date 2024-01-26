import mysql.connector
from configparser import ConfigParser


def conectar_a_mysql():
    """_summary_

    Returns:
        _type_: connection
        la conexion a la base de datos
    """
    config = ConfigParser()
    config.read('app\\config.properties')

    try:
        # Crear una conexión
        conn = mysql.connector.connect(
            user=config.get('MySQL', 'mysql_user'),
            password=config.get('MySQL', 'mysql_password'),
            host=config.get('MySQL', 'mysql_host'),
            database=config.get('MySQL', 'mysql_database'),
            port=config.get('MySQL', 'mysql_port')
        )

        if conn.is_connected():
            return conn

    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")
        return None


def create_table():
    """_summary_
    
    _type_: Description
    crea estructura de la Tabla en la base de datos
    
    """
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()

            command = """
            CREATE TABLE IF NOT EXISTS Juegos(
                id INT NOT NULL AUTO_INCREMENT,
                nombre Varchar(255) NOT NULL,
                plataforma Varchar(255),
                year INT(4),
                genero Varchar(255),
                publisher VARCHAR(255),
                V_NA Double NOT NULL,
                V_EU Double NOT NULL,
                V_JP Double Not NULL,
                V_other Double NOT NULL,
                V_Global Double NOT NULL,
                PRIMARY KEY(id)
            )
            """
            cursor.execute(command)
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
