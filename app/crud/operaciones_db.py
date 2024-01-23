from app.db.conexion_db import conectar_a_mysql
import mysql


def listar_juegos_db():
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            sql = 'SELECT id,nombre,plataforma,year,genero,publisher FROM Juegos'
            cursor.execute(sql)
            lista_j = cursor.fetchall()
            return lista_j

        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
