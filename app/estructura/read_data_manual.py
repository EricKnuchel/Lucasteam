from app.estructura.catalogo import Juego, Juegos

def leer_datos_manual():
    rank = len(Juegos.lista_juegos)+2
    nom = input("Escriba el nombre del juego: ")
    plataf = input("Introduzca una consola: ")
    year = input("Introduzca el año de salida del juego: ")
    genero = input("Introduzca el género del juego: ")
    editor = input("Introduzca el nombre del editor: ")
    v_na = input("Introduzca el número de ventas en North America: ")
    v_eu = input("Introduzca el número de ventas en Europa: ")
    v_jp = input("Introduzca el número de ventas en Japón: ")
    v_otros = input("Introduzca el número de ventas en el resto del mundo: ")
    v_gl = input("Introduzca el número de ventas a nivel global: ")
    
    j = Juego(rank, nom, plataf, year, genero, editor, v_na, v_eu, v_jp, v_otros, v_gl)
    
    return print("Elemento agregado a la lista") if Juegos.alta_juego(j) else print("Elemento no agregado a la lista")
        