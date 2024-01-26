import logging
import re

logger = logging.getLogger("").getChild(__name__)


def juego_repetido(j, l_j):
    """_summary_

    Args:
        j = juego(_type_): _description_
        l_j = lista_juegos (_type_): _description_

    Returns:
        _type_: _Boolean_
        true si el juego existe o false si el juego no existe
    """
    repetido = False
    for i in l_j:
        if i.name == j.name and i.plataf == j.plataf and i.year == j.year:
            logger.info(f"ID {i.rank}-El juego ya existe en la lista")
            repetido = True
            return repetido

    return repetido


def campos_correctos(j):
    """_summary_

    Args:
        j (_type_): _description_

    Returns:
        _type_: _Boolean_
        true si todos los campos son correctos o false si no lo son
    """
    correcto = False
    lista_atrib = j.listar_atrib()
    caracteres_no_permitidos = r"%$#@¨{}[]\^`"
    punto_coma_guion = [";", "_"]
    ident = j.rank
    for a in lista_atrib:
        if str(a).isspace() or str(a) == "":
            logger.info(f"ID {ident}-No puede haber campos vacíos")
            return correcto

        for i in punto_coma_guion:
            if i in str(a):
                logger.info(f"ID {ident}-{a} no puede contener '{i}'")
                return correcto

        if re.search(f"[{re.escape(caracteres_no_permitidos)}]", str(a)):
            logger.info(f"ID {ident}-El elemento {a} contiene caracteres no perimitidos")
            return correcto

    correcto = True
    return correcto


def validar_nombre(n):
    """_summary_

    Args:
        n = nombre del juego (_type_): _description_
        
    Returns:
        _type_: _Boolean_ , _description_
        true si el nombre es correcto o false si no lo es 
        y el nombre de el juego en los dos casos
    """
    correcto = False
    letras_n = list(n)
    if len(letras_n) < 2:
        logger.info("El nombre debe tener mas de dos letras")
        return correcto, n
    else:
        n = n.capitalize()
        correcto = True
        return correcto, n


def validar_ventas(v):
    """_summary_

    Args:
        v = ventas (_type_): _description_

    Returns:
        _type_: _Boolean_, _list_
        true si el numero de las ventas 
        tiene el formato correcto es correcto 
        o false si no lo tiene
        y la lista de la venta
    """
    correcto = False
    salida = False
    i = 0
    top = 5

    while not salida:
        try:
            vt = int(v[i])

            if vt < 0:
                logger.info("El numero no puede ser negativo")
                return correcto, v
            else:
                v[i] = vt

        except:
            try:
                vt = float(v[i])

                if vt < 0:
                    logger.info("El numero no puede ser negativo")
                    return correcto, v
                else:
                    vt = format(vt, ".2f")
                    v[i] = vt
            except ValueError:
                logger.error("No es un numero")
            except Exception as e:
                logger.error(f"Ha orcurrido un error: {e}")
                return correcto, v
        i += 1
        salida = (i == top)

    correcto = True
    return correcto, v


def eliminar_datos_db(d):
    """_summary_

    Args:
        d = datos(_type_): _description_
        lita de los datos de el csv

    Returns:
        _type_: _Boolean_
        true si cumple las espesificaciones o false si no las cumple
    """
    add = False
    if d[3] == 'N/A':
        logger.info(f"ID {d[3]}-El juego con tiene un year nulo")
        return add
    else:
        add = True
        return add


def validar_year_par(year):
    """_summary_

    Args:
        year (_type_): _description_

    Returns:
        _type_: _list_
        lista filtrada en años pares
    """
    for y in year:
        if y[3] % 2 != 0:
            logger.info(f"ID {y[0]}-Año impar encontrado: {y[3]}")
            year.remove(y)

    return year
