class Juegos:
    lista_juegos = []

    @classmethod
    def inser_data(cls, data):
        j = Juego(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        return cls.lista_juegos.append(j)
    
    
    @classmethod
    def show_siglo_xx(cls):
        juegos_siglo_xx = [juego for juego in cls.lista_juegos if str(1900) <= juego.year <= str(1999)]
        return juegos_siglo_xx

    def show_games_siglo_xx():
        juego_instance = Juegos
        siglo_xx_games = juego_instance.show_siglo_xx()
        for juego in siglo_xx_games:
            print(f"{juego.rank}: {juego.name}, Year: {juego.year}")
        

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
    
    # Este es un metodo de Python que se usa para definir el comportamiento de el operador de igualdad (==)
    def __eq__(self, other):
        """# verificamos si other es una instancia de la clase Juegos
        si no lo es no se considerarian iguales y retorna false"""
        if not isinstance(other, Juego):
            return False
        return vars(self) == vars(other)
