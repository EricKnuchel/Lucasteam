import unittest
from app.estructura.catalogo import Juego, Juegos
from app.crud.operaciones import delete_juego, update_juegos, listar_juegos_db 
from app.db.consultas_db import conectar_a_mysql,show_genere, show_siglo_xx
from app.crud.operaciones import delete_juego, update_juegos



# Prueba unitaria de la funsion insert_data
class TestJuegos(unittest.TestCase):
    def test_inser_data(self):
        test_data = ['1', 'Example game', 'PlatformX', '2022', 'Action', 'PublisherY', '10.00', '5.00', '2.00', '1.00',
                     '18.00']

        Juegos.inser_data(test_data)

        actual_result = Juegos.lista_juegos

        expected_result = [Juego(*test_data)]

        self.assertEqual(actual_result, expected_result)


class TestDeleteJuego(unittest.TestCase):

    def test_delete_juego_exitoso(self):
        # Supongamos que 'id_a_eliminar' es un ID válido que quieres probar
        resultado = delete_juego(1301) # cambiar ide siempre que se use la pruea unitaria
        self.assertTrue(resultado, "La eliminación debería ser exitosa")

    def test_delete_juego_fallido(self):
        # Supongamos que 'id_inexistente' es un ID que no existe y quieres probar la caída
        resultado = delete_juego(17000)
        self.assertFalse(resultado, "La eliminación debería fallar ya que el juego no existe") 


class TestUpdateJuegos(unittest.TestCase):
    def test_update_juegos(self):
        # Supongamos que tienes un juego con el id=1 en tu base de datos
        # Cambia los valores según tu base de datos y la entrada que desees probar
        id = 1
        nombre = "NuevoNombre"
        plataforma = "NuevaPlataforma"
        year = 2022
        genero = "NuevoGenero"
        publisher = "NuevoPublisher"

        # Llama a la función de actualización
        update_juegos(id, nombre, plataforma, year, genero, publisher)

        # Ahora, verifica si los datos fueron actualizados correctamente
        # Recupera los datos actualizados de la base de datos y compáralos con los valores esperados
        conn = conectar_a_mysql()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Juegos WHERE id=%s", (id,))
        updated_data = cursor.fetchone()
        conn.close()

        # Verifica las actualizaciones
        self.assertIsNotNone(updated_data, "No se encontraron datos actualizados")
        self.assertEqual(updated_data[1], nombre, "El nombre no coincide")
        self.assertEqual(updated_data[2], plataforma, "La plataforma no coincide")
        self.assertEqual(updated_data[3], year, "El año no coincide")
        self.assertEqual(updated_data[4], genero, "El género no coincide")
        self.assertEqual(updated_data[5], publisher, "El publisher no coincide")
        
    def test_update_juegos_fallido(self):
        # Supongamos que estos son valores inválidos o un ID que no existe que quieres probar
        id_inexistente = 17000
        nombre_nuevo = "Nuevo Nombre"
        plataforma_nueva = "Nueva Plataforma"
        year_nuevo = 2025
        genero_nuevo = "Nuevo Genero"
        publisher_nuevo = "Nuevo Publisher"

        resultado = update_juegos(id_inexistente, nombre_nuevo, plataforma_nueva, year_nuevo, genero_nuevo,
                                  publisher_nuevo)
        self.assertFalse(resultado, "La actualización debería fallar ya que el juego con el ID proporcionado no existe")
        

class TestListarDatosDB(unittest.TestCase):
    #Se comprueba que los datos devueltos traen todos los campos
    def test_campos_lista_db(self):
        num_campos_esperados = 6
        lista_db = listar_juegos_db()
        
        for d in lista_db:
            self.assertEqual(len(d),num_campos_esperados)

        
class TestFiltrarGenero(unittest.TestCase):
    
    def test_lista_filtrar_genero(self):
        genero_esperado = "Sports"
        lista_gen = show_genere(genero_esperado)
        resultados_filtrados = [item for item in lista_gen if genero_esperado in item]
        
        self.assertTrue(resultados_filtrados, f"No se encontraron elementos con el género {genero_esperado}")
        for g in resultados_filtrados:
            self.assertIn(genero_esperado, g, f"El género {genero_esperado} no está presente en el elemento {g}")

class TestShowSigloXX(unittest.TestCase):
    def test_show_siglo_xx_success(self):
        # Llama a la función
        result = show_siglo_xx()

        # Verifica que la función devuelva una lista no vacía
        self.assertTrue(result)

        # Verifica que todos los datos estan entre 1900 y 1999
        for juego in result:
            year = juego[3]
            self.assertTrue(1900 <= year <= 1999)
            self.assertEqual(len(juego),11)


if __name__ == '__main__':
    unittest.main()
