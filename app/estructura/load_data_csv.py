import csv
import pandas as pd
from app.estructura.catalogo import Juegos
from app.db.conexion_db import conectar_a_mysql
from app.validaciones.validaciones import eliminar_datos_db


def load_list():
    try:
        with open('datos/vgsales.csv', 'r') as f:
            lectura = csv.reader(f)
            next(lectura)
            for l in lectura:
                lista = l
                Juegos.inser_data(lista)

    except FileNotFoundError:
        print("Archivo no encontrado")
    except IOError:
        print("Error al leer el fichero.")
    except csv.Error:
        print("Error al leer los datos del CSV")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def load_db():
    conn = conectar_a_mysql()

    if conn:
        cursor = conn.cursor()

    try:
        sql = "SELECT COUNT(id) FROM Juegos"
        cursor.execute(sql)
        num_dat = cursor.fetchone()

        with open('datos/vgsales.csv', 'r') as f:
            lectura = csv.reader(f)
            next(lectura)
            for l in lectura:
                if num_dat[0] == 0:
                    if eliminar_datos_db(l):
                        sql = "INSERT INTO Juegos (nombre, plataforma, year, genero, publisher, V_NA, V_EU, V_JP, V_other, V_Global) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = (
                            l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9],
                            l[10])

                        cursor.execute(sql, val)

                        conn.commit()

    except FileNotFoundError:
        print("Archivo no encontrado")
    except IOError:
        print("Error al leer el fichero.")
    except csv.Error:
        print("Error al leer los datos del CSV")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        cursor.close()
        conn.close()


def load_dataframe():
    data = pd.read_csv('datos/vgsales.csv')
    return data

    