from app.estructura.read_data_csv import leer_datos
from gui.interfaz import run_gui
from app.crud.operaciones import update_juegos, delete_juego, get_info_for_id

def main():
    leer_datos()
    run_gui()
    
    
if __name__ == '__main__':
    main()