import unittest
from app.estructura.catalogo import Juego, Juegos

# Prueba unitaria de la funsion insert_data
class TestJuegos(unittest.TestCase):
    def test_inser_data(self):
        test_data = ['1', 'Example Game', 'PlatformX', '2022', 'Action', 'PublisherY', '10.0', '5.0', '2.0', '1.0', '18.0']
        
        Juegos.inser_data(test_data)

        actual_result = Juegos.lista_juegos

        expected_result = [Juego(*test_data)]

        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()