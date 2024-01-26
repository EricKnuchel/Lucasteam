from app.db.conexion_db import conectar_a_mysql


def update_juegos(id, nombre, plataforma, year, genero, publisher):
    """_summary_

    Args:
        id (_type_): _description_
        nombre (_type_): _description_
        plataforma (_type_): _description_
        year (_type_): _description_
        genero (_type_): _description_
        publisher (_type_): _description_
        
        Funcion que se encarga de actualizar los juegos
        haciendo referencia a su ID
    """
    conn = conectar_a_mysql()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "UPDATE Juegos SET nombre=%s, plataforma=%s, year=%s, genero=%s, publisher=%s WHERE id=%s"

            cursor.execute(sql, (nombre, plataforma, year, genero, publisher, id))
            conn.commit()
            print("Registro actualizado exitosamente!")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar el juego", str(e))

        finally:
            cursor.close()
            conn.close()


def delete_juego(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: Boolean
    """
    conn = conectar_a_mysql()
    if conn:
        cursor = conn.cursor()

        sql = "DELETE from Juegos WHERE id=%s"

        try:
            cursor.execute(sql, (id,))
            if cursor.rowcount > 0:
                conn.commit()
                print("Eliminación exitosa")
                return True
            else:
                conn.rollback()
                print("El juego con ID={} no existe".format(id))
                return False

        except Exception as e:
            conn.rollback()
            print("Error al eliminar el juego", str(e))

        finally:
            cursor.close()
            conn.close()
    else:
        return False


def get_info_for_id(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
        la informacion de el juego correspondiente al ID
    """
    conn = conectar_a_mysql()
    if conn:
        cursor = conn.cursor()

        try:
            sql = "select * from Juegos WHERE id=%s"
            cursor.execute(sql, (id,))
            res = cursor.fetchone()
            if res:
                return res
            else:
                print(f"Error, al obtener la informacion de este id: {id}")

        except Exception as e:
            print("Error al obtner la info", str(e))

        finally:
            cursor.close()
            conn.close()


def listar_juegos_db():
    """_summary_

    Returns:
        _type_: Lista
        
        Una lista con los juegos 
        extraidas desde la base de datos 
    """
    conn = conectar_a_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            sql = 'SELECT id,nombre,plataforma,year,genero,publisher FROM Juegos'
            cursor.execute(sql)
            lista_j = cursor.fetchall()
            return lista_j
        finally:
            cursor.close()
            conn.close()
