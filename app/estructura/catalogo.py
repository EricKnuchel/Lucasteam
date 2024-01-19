class Juegos:
    lista_juegos = {}

    @classmethod
    def inser_data(cls, data):
        j = Juego(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        cls.lista_juegos[j.rank] = j
        
    @classmethod
    def alta_juego(cls, j):
        alta = False
        
        return True
        


class Juego:
    def __init__(self, rank, name, plataf, year, genero, editor, v_na, v_eu, v_jp, v_otras, v_glob):
        self.rank = rank
        self.name = name
        self.plataf = plataf
        self.year = year
        self.genero = genero
        self.editor = editor
        self.v_na = v_na
        self.v_eu = v_eu
        self.v_jp = v_jp
        self.v_otras = v_otras
        self.v_glob = v_glob