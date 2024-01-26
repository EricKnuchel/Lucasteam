import csv
import logging
import pandas as pd
from app.estructura.catalogo import Juegos
from app.db.conexion_db import conectar_a_mysql
from app.validaciones.validaciones import eliminar_datos_db
from exception.exception import DemoException

logger = logging.getLogger("").getChild(__name__)

def load_list():
    try:
        pass
    except FileNotFoundError:
        logger.error("Archivo no encontrado")
    except IOError as io:
        logger.error(f"Error:{io}")
    except csv.Error:
        logger.error("Error al leer los datos del CSV")
    except Exception as e:
        logger.error(e)


def load_db():
    conn = conectar_a_mysql()

    if conn:
        cursor = conn.cursor()

    try:
        pass

    except FileNotFoundError:
        logger.error("Archivo no encontrado")
    except IOError:
        logger.error("Error al leer el fichero.")
    except csv.Error:
        logger.error("Error al leer los datos del CSV")
    except Exception as e:
        logger.error(f"Ha ocurrido un error: {e}")
    finally:
        cursor.close()
        conn.close()


def load_dataframe():
    data = pd.read_csv('datos/vgsales.csv')
    print(data)
    return data
