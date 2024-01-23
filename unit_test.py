import unittest
from app.estructura.catalogo import Juego, Juegos
from app.crud.operaciones import delete_juego, update_juegos
from app.db.conexion_db import conectar_a_mysql


# Prueba unitaria de la funsion insert_data
class TestJuegos(unittest.TestCase):
    def test_inser_data(self):
        test_data = ['2', 'Example game', 'PlatformX', '2022', 'Action', 'PublisherY', '10.00', '5.00', '2.00', '1.00',
                     '18.00'] 

        Juegos.inser_data(test_data)

        actual_result = Juegos.lista_juegos

        expected_result = [Juego(*test_data)]

        self.assertEqual(actual_result, expected_result)


class TestDeleteJuego(unittest.TestCase):

    def test_delete_juego_exitoso(self):
        # Supongamos que 'id_a_eliminar' es un ID válido que quieres probar
        resultado = delete_juego(88) # cambiar ide siempre que se use la pruea unitaria
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


if __name__ == '__main__':
    unittest.main()
