import re


def juego_repetido(j, l_j):
    repetido = False
    for i in l_j:
        if i.name == j.name and i.plataf == j.plataf and i.year == j.year:
            repetido = True
            return repetido

    return repetido


def campos_correctos(j):
    correcto = False
    lista_atrib = j.listar_atrib()
    caracteres_no_permitidos = r"%$#@¨{}[]\^`"
    punto_coma_guion = [";", "_"]
    for a in lista_atrib:
        if str(a).isspace() or str(a) == "":
            return correcto, print("No puede haber campos vacíos")

        for i in punto_coma_guion:
            if i in str(a):
                return correcto, print(f"{a} no puede contener '{i}'")

        if re.search(f"[{re.escape(caracteres_no_permitidos)}]", str(a)):
            return correcto, print(f"El elemento {a} contiene caracteres no perimitidos")

    correcto = True
    return correcto


def validar_nombre(n):
    correcto = False
    letras_n = list(n)
    if len(letras_n) < 2:
        return correcto, n
    else:
        n = n.capitalize()
        correcto = True
        return correcto, n


def validar_ventas(v):
    correcto = False
    salida = False
    i = 0
    top = 5

    while not salida:
        try:
            vt = int(v[i])

            if vt < 0:
                print("El número no puede ser negativo")
                return correcto, v
            else:
                v[i] = vt

        except:
            try:
                vt = float(v[i])

                if vt < 0:
                    print("El número no puede ser negativo")
                    return correcto, v
                else:
                    vt = format(vt, ".2f")
                    v[i] = vt
            except ValueError:
                print("No es un número")
            except Exception as e:
                print(f"A orcurrido un error: {e}")
                return correcto, v
        i += 1
        salida = (i == top)

    correcto = True
    return correcto, v

def eliminar_datos_db(d):
    add = False
    if d[3] == 'N/A':
        return add
    else:
        add = True
        return add