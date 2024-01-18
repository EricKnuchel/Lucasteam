import unittest
from app.estructura.catalogo import Juego, Juegos

# Prueba unitaria de la funsion insert_data
class TestJuegos(unittest.TestCase):
    def test_inser_data(self):
        # Create test data
        test_data = ['1', 'Example Game', 'PlatformX', '2022', 'Action', 'PublisherY', '10.0', '5.0', '2.0', '1.0', '18.0']

        # Call inser_data with the test data
        Juegos.inser_data(test_data)

        # Replace Juegos.lista_juegos with the actual attribute in your Juegos class
        actual_result = Juegos.lista_juegos

        # Define the expected result based on the test data
        expected_result = [Juego(*test_data)]

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()