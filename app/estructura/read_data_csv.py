import csv
from app.estructura.catalogo import Juegos


path = 'datos/vgsales.csv'
def leer_datos():
    with open(path, 'r') as f:
        lectura = csv.reader(f)
        for l in lectura:
            lista = l
            Juegos.inser_data(lista)
        x = Juegos.lista_juegos
        print(x)
