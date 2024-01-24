from app.db.conexion_db import create_table
from app.estructura.load_data_csv import leer_datos
from gui.interfaz import run_gui



def main():
    create_table()
    leer_datos()
    run_gui()

if __name__ == '__main__':
    main()
