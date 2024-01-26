from app.estructura.load_data_csv import load_dataframe


def listado_pandas():
    """_summary_

    Returns:
        Los 30 primeros datos leidos por la libreria 'Pandas'
    """
    data = load_dataframe()  # llamada al metodo que devuelve los datos leidos por la libreria 'Pandas'
    data.set_index('Rank', inplace=True)  # asignamos la columna Rank como index principal
    return data.loc[:30][['Name', 'Platform', 'Year', 'Genre', 'Publisher']]
