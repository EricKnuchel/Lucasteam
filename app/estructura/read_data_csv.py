import csv
from app.estructura.catalogo import Juegos

def leer_datos():
    try:
        with open('datos/vgsales.csv', 'r') as f:
            lectura = csv.reader(f)
            next(lectura)
            for i, l in enumerate(lectura):
                if i >= 1000:
                    break
                lista = l
                Juegos.inser_data(lista)
            # x = Juegos.lista_juegos
            # print(x[0].name)
            print("Si se imprime este mensaje funciona correcto.")

    except FileNotFoundError:
        print("Archivo no encontrado")
    except IOError:
        print("Error al leer el fichero.")
    except csv.Error:
        print("Error al leer los datos del CSV")
    except Exception as e:
        print(f"A orcurrido un error: {e}")

