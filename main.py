from app.estructura.read_data_csv import leer_datos
from app.estructura.read_data_manual import leer_datos_manual


def main():
    leer_datos()
    leer_datos_manual()

if __name__ == '__main__':
    main()