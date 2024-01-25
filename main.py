from app.db.conexion_db import create_table
from app.estructura.load_data_csv import load_db,load_list
from gui.interfaz import run_gui
import logging
    
logging.basicConfig(filename='log/proyecto_juegos_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode = "w")


def main():
    create_table()
    load_db()
    load_list()
    run_gui()

if __name__ == '__main__':
    main()
