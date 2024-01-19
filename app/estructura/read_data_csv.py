import csv
from app.estructura.catalogo import Juegos


path = 'datos/vgsales.csv'
def leer_datos():
    with open(path, 'r') as f:
        lectura = csv.reader(f)
        next(lectura)
        for i, l in enumerate(lectura):
            if i >= 10:
                break
            lista = l
            Juegos.inser_data(lista)