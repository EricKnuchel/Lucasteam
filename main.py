import logging

from app.db.conexion_db import create_table
from app.estructura.load_data_csv import load_db, load_list
from gui.interfaz import run_gui

# Creación del archivo donde se alojaran los logs o registros del proyecto
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s [%(levelname)s] %(message)s',
                    filename='log/proyecto_juegos_log.log', filemode="w")


def main():
    """ Función controladora de la app,
        se encarga de hacer las llamadas a las distintas funciones
        que leen datos,
        tambien se hace la llamada a la interfaz principal
    """
    create_table()
    load_db()
    load_list()
    run_gui()


if __name__ == '__main__':
    main()
