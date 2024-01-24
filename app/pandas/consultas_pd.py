from app.estructura.load_data_csv import load_dataframe


def listado_pandas():
    data = load_dataframe()
    data.set_index('Rank', inplace=True)
    print(data.loc[:25][['Name', 'Platform', 'Year', 'Genre', 'Publisher']])
    return data.loc[:25][['Name', 'Platform', 'Year', 'Genre', 'Publisher']]
