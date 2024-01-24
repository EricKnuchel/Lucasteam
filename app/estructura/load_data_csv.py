import csv
import pandas as pd
from app.estructura.catalogo import Juegos
from app.db.conexion_db import conectar_a_mysql


def leer_datos():
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
                lista = l
                Juegos.inser_data(lista)

                if num_dat[0] == 0:
                    sql = "INSERT INTO Juegos (nombre, plataforma, year, genero, publisher, V_NA, V_EU, V_JP, V_other, V_Global) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (
                        lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
                        lista[10])

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

    