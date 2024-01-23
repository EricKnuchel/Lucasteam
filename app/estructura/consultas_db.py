from app.db.conexion_db import conectar_a_mysql
import mysql


def show_genere(gen):
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            sql = 'SELECT id, nombre, plataforma, year, genero, publisher FROM Juegos WHERE genero LIKE %s'
            val = (gen, )
            cursor.execute(sql, val)
            lista_gen = cursor.fetchall()
            
            return lista_gen
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
