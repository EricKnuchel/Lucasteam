from app.validaciones import validaciones as val

class Juegos:
    lista_juegos = []

    @classmethod
    def inser_data(cls, data):
        j = Juego(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        
        if Juegos.alta_juego(j):
            return cls.lista_juegos.append(j)
        else:
            del j
            print("El juego no se añadió a la lista")
    
    @classmethod
    def alta_juego(cls,j):
        alta = False
        
        #validación de campos vacios
        if not val.juego_repetido(j, Juegos.lista_juegos):
            if val.campos_correctos(j):
                nom_correcto, nom = val.validar_nombre(j.name)
                if nom_correcto:
                    j.name = nom
                    list_vent = [j.v_na, j.v_eu, j.v_jp, j.v_otras, j.v_glob]
                    vent_correcto, vent = val.validar_ventas(list_vent)
                    if vent_correcto:
                        j.v_na = vent[0]
                        j.v_eu = vent[1]
                        j.v_jp = vent[2]
                        j.v_otras = vent[3]
                        j.v_glob = vent[4]
                        alta = True
        else:
            print("El juego ya existe")
        
        return alta

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
        
    def listar_atrib(self):
        lista_atrib = [self.rank, self.name, self.plataf, self.year, self.genero, self.editor, self.v_na, self.v_eu, self.v_jp, self.v_otras, self.v_glob]
        return lista_atrib
    
    # Este es un metodo de Python que se usa para definir el comportamiento de el operador de igualdad (==)
    def __eq__(self, other):
        """# verificamos si other es una instancia de la clase Juegos
        si no lo es no se considerarian iguales y retorna false"""
        if not isinstance(other, Juego):
            return False
        return vars(self) == vars(other)
