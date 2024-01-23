import unittest
from app.estructura.catalogo import Juego, Juegos
from app.crud.operaciones import delete_juego, update_juegos
from app.db.consultas_db import show_siglo_xx


# Prueba unitaria de la funsion insert_data
class TestJuegos(unittest.TestCase):
    def test_inser_data(self):
        test_data = ['1', 'Example Game', 'PlatformX', '2022', 'Action', 'PublisherY', '10.0', '5.0', '2.0', '1.0',
                     '18.0']

        Juegos.inser_data(test_data)

        actual_result = Juegos.lista_juegos

        expected_result = [Juego(*test_data)]

        self.assertEqual(actual_result, expected_result)


class TestDeleteJuego(unittest.TestCase):

    def test_delete_juego_exitoso(self):
        # Supongamos que 'id_a_eliminar' es un ID válido que quieres probar
        resultado = delete_juego(14)
        self.assertTrue(resultado, "La eliminación debería ser exitosa")

    def test_delete_juego_fallido(self):
        # Supongamos que 'id_inexistente' es un ID que no existe y quieres probar la caída
        resultado = delete_juego(17000)
        self.assertFalse(resultado, "La eliminación debería fallar ya que el juego no existe") 


class TestUpdateJuegos(unittest.TestCase):

    def test_update_juegos_exitoso(self):
        # Supongamos que estos son valores válidos que quieres probar
        id_a_actualizar = 12
        nombre_nuevo = "Nuevo Nombre x"
        plataforma_nueva = "Nueva Plataforma"
        year_nuevo = 2025
        genero_nuevo = "Nuevo Genero"
        publisher_nuevo = "Nuevo Publisher"

        resultado = update_juegos(id_a_actualizar, nombre_nuevo, plataforma_nueva, year_nuevo, genero_nuevo,
                                  publisher_nuevo)
        self.assertTrue(resultado, "La actualización debería ser exitosa")

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
