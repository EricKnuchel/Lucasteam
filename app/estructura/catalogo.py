import logging

from app.validaciones import validaciones as val

logger = logging.getLogger("").getChild(__name__)


class Juegos:
    """_summary_

    clase contenedora de lops metodos
    que se encargan de insertar los datos 
    en la lista
    """
    lista_juegos = []

    @classmethod
    def inser_data(cls, data):
        """_summary_

        Args:
            data (_type_): _description_
            los datos cargargados desde el csv

        Returns:
            _type_: list
            la lista con sus datos incertados
        """
        j = Juego(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])

        if Juegos.alta_juego(j):
            return cls.lista_juegos.append(j)
        else:
            logger.warning(f"ID {j.rank}-El juego no se ha agregado a la lista")

    @classmethod
    def alta_juego(cls, j):
        """_summary_

        Args:
            j = juego (_type_): _description_

        Returns:
            _type_: _Boolean_
        """
        alta = False

        # validación de campos vacios
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

        return alta

    @classmethod
    def __str__(cls):
        """_summary_

        Returns:
            _type_: _lista_
            recorriendo cada objeto y convirtiendolo a string
        """
        return '\n'.join(str(juego) for juego in cls.lista_juegos)


class Juego:
    def __init__(self, rank, name, plataf, year, genero, editor, v_na, v_eu, v_jp, v_otras, v_glob):
        """_summary_

        Args:
            rank (_type_): _description_
            name (_type_): _description_
            plataf (_type_): _description_
            year (_type_): _description_
            genero (_type_): _description_
            editor (_type_): _description_
            v_na (_type_): _description_
            v_eu (_type_): _description_
            v_jp (_type_): _description_
            v_otras (_type_): _description_
            v_glob (_type_): _description_
        """
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
        """_summary_

        Returns:
            _type_: _lista_
            con todos los atributos dentro
        """
        lista_atrib = [self.rank, self.name, self.plataf, self.year, self.genero, self.editor, self.v_na, self.v_eu,
                       self.v_jp, self.v_otras, self.v_glob]
        return lista_atrib

    def __str__(self):
        """_summary_

        Returns:
            _type_: _lista_
            recorriendo cada objeto y convirtiendolo a string
        """
        return f"Juego(rank={self.rank}, name={self.name}, plataf={self.plataf}, year={self.year}, genero={self.genero}, " \
               f"editor={self.editor}, v_na={self.v_na}, v_eu={self.v_eu}, v_jp={self.v_jp}, v_otras={self.v_otras}, v_glob={self.v_glob})"

    # Este es un metodo de Python que se usa para definir el comportamiento de el operador de igualdad (==)
    def __eq__(self, other):
        """verificamos si other(una region) es una instancia de la clase Juegos
        si no lo es no se considerarian iguales y retorna false
        """
        if not isinstance(other, Juego):
            return False
        return vars(self) == vars(other)
