from app.db.conexion_db import conectar_a_mysql
import mysql


def show_genere(gen):
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            sql = 'SELECT id, nombre, plataforma, year, genero, publisher FROM Juegos WHERE genero LIKE %s'
            val = (gen,)
            cursor.execute(sql, val)
            lista_gen = cursor.fetchall()

            return lista_gen
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()


def show_siglo_xx():
    conn = conectar_a_mysql()

    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return []

    juegos_siglo_xx = []

    try:
        query = "SELECT * FROM Juegos WHERE year >= 1900 AND year < 2000"
        cursor = conn.cursor()
        cursor.execute(query)
        juegos_siglo_xx = cursor.fetchall()
        return juegos_siglo_xx

    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")

    finally:
        cursor.close()
        conn.close()

    return juegos_siglo_xx
