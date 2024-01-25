from app.db.conexion_db import create_table
from app.estructura.load_data_csv import load_db, load_list
from gui.interfaz import run_gui


def main():
    create_table()
    load_db()
    load_list()
    run_gui()


if __name__ == '__main__':
    main()
