from app.estructura.read_data_csv import leer_datos
from gui.interfaz import run_gui
from app.estructura.catalogo import Juego,Juegos

def main():
    leer_datos()
    j = Juego("1","Wii sports","Wii","2007","das","asdas","23", "0.45", "2", "34.5", "76")
    alta = Juegos.alta_juego(j)
    run_gui()
    

if __name__ == '__main__':
    main()