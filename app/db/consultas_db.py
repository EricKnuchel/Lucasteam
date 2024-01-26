import mysql

from app.db.conexion_db import conectar_a_mysql


def show_genere(gen):
    """_summary_

    Args:
        gen (_type_): _description_
        la entrada es el generos a filtrar

    Returns:
        _type_: _list_
        una lista con los juegos que coninciden con el genero
    """
    conn = conectar_a_mysql()  # conectando con la base de datos
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
    """_summary_

    Returns:
        _type_: _list_
        una lista de todos los juegos del siglo XX
    """
    conn = conectar_a_mysql()  # conectando con la base de datos

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


def show_platform():
    """_summary_

    Returns:
        _type_: _list_
        una lista de todos los juegos que coincidan con el Editor especificado
    """
    conn = conectar_a_mysql()  # conectando con la base de datos

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


def show_year_par():
    """_summary_

    Returns:
        _type_: _list_
        una lista de todos los juegos que coincidan con los años pares
    """
    conn = conectar_a_mysql()  # conectando con la base de datos

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


def show_max_venta():
    """_summary_

    Returns:
        _type_: _list_
        una lista de todos los juegos mas vendidos a nivel global
    """
    conn = conectar_a_mysql()  # conectando con la base de datos

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


def show_max_venta_regional(region):
    """_summary_

    Args:
        region (_type_): _description_

    Returns:
        _type_: _list_
        una lista de los juegos mas vendidos por la region espesificada
    """
    conn = conectar_a_mysql()  # conectando con la base de datos

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


def show_media():
    """_summary_

    Returns:
        _type_: _list_
        una lista de los juegos con la media de venta 
        superior a la media de venta en Europa
    """
    conn = conectar_a_mysql()  # conectando con la base de datos

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

    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")

    finally:
        cursor_media.close()
        cursor.close()
        conn.close()

    return juegos_media


def show_editor(e):
    """_summary_

    Args:
        e (_type_): _description_

    Returns:
        _type_: _list_
        una lista de editores con sus juegos asociados 
    """
    conn = conectar_a_mysql()  # conectando con la base de datos
    if conn:
        try:
            cursor = conn.cursor()
            sql = 'SELECT id, nombre, publisher FROM Juegos WHERE publisher LIKE %s'
            val = (e,)
            cursor.execute(sql, val)
            lista_edi = cursor.fetchall()

            return lista_edi
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
        finally:
            cursor.close()
            conn.close()
