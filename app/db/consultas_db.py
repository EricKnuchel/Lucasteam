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

    if conn:

        juegos_siglo_xx = []

        try:
            query = "SELECT id, nombre, plataforma, year, genero, publisher FROM Juegos WHERE year >= 1900 AND year < 2000"
            cursor = conn.cursor()
            cursor.execute(query)
            juegos_siglo_xx = cursor.fetchall()
            return juegos_siglo_xx

        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            cursor.close()
            conn.close()
    else:

        print("No se pudo conectar a la base de datos.")
        return []

    return juegos_siglo_xx


def show_platform():
    conn = conectar_a_mysql()

    if conn:

        nintendo = []

        try:
            query = "SELECT id, nombre, plataforma, year, genero, publisher FROM Juegos WHERE publisher = 'Nintendo'"
            cursor = conn.cursor()
            cursor.execute(query)
            nintendo = cursor.fetchall()
            return nintendo

        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            cursor.close()
            conn.close()
    else:

        print("No se pudo conectar a la base de datos.")
        return []

    return nintendo


def show_year_par():
    conn = conectar_a_mysql()

    if conn:

        juegos_par = []

        try:
            query = "SELECT id, nombre, plataforma, year, genero, publisher FROM Juegos WHERE MOD(year, 2) = 0"
            cursor = conn.cursor()
            cursor.execute(query)
            juegos_par = cursor.fetchall()
            return juegos_par

        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            cursor.close()
            conn.close()
    else:

        print("No se pudo conectar a la base de datos.")
        return []

    return juegos_par


def show_max_venta():
    conn = conectar_a_mysql()  # Asumiendo que tienes una función llamada conectar_a_mysql()

    if conn:

        juegos_max_venta = []

        try:
            query = "SELECT id, nombre, plataforma, year, publisher, v_global FROM Juegos ORDER BY v_global DESC LIMIT 5"
            cursor = conn.cursor()
            cursor.execute(query)
            juegos_max_venta = cursor.fetchall()
            return juegos_max_venta

        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            cursor.close()
            conn.close()

    else:

        print("No se pudo conectar a la base de datos.")
        return []

    return juegos_max_venta

def show_max_venta_regional(region):
    
    conn = conectar_a_mysql()  # Asumiendo que tienes una función llamada conectar_a_mysql()

    if conn:

        juegos_max_venta = []

        try:
            query = f"SELECT id, nombre, plataforma, year, publisher, {region} FROM Juegos ORDER BY {region} DESC LIMIT 5"
            cursor = conn.cursor()
            cursor.execute(query)
            juegos_max_venta = cursor.fetchall()
            return juegos_max_venta

        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            cursor.close()
            conn.close()

    else:

        print("No se pudo conectar a la base de datos.")
        return []

    return juegos_max_venta


def show_media():
    conn = conectar_a_mysql()  # Asumiendo que tienes una función llamada conectar_a_mysql()

    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return []

    juegos_media = []

    try:
        # Calcular la media de las ventas globales
        query_media = "SELECT AVG(V_EU) FROM Juegos"
        cursor_media = conn.cursor()
        cursor_media.execute(query_media)
        media = cursor_media.fetchone()[0]

        # Seleccionar los juegos por encima de la media
        query_juegos_por_encima_de_media = "SELECT id, nombre, plataforma, year, publisher, V_EU FROM Juegos WHERE V_EU > %s"
        cursor = conn.cursor()
        cursor.execute(query_juegos_por_encima_de_media, (media,))
        juegos_media = cursor.fetchall()
        # return juegos_media

    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")

    finally:
        cursor_media.close()
        cursor.close()
        conn.close()

    return juegos_media


def show_editor(e):
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            sql = 'SELECT id, nombre, publisher FROM Juegos WHERE publisher LIKE %s'
            val = (e,)
            cursor.execute(sql, val)
            lista_gen = cursor.fetchall()

            return lista_gen
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
