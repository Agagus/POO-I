import unittest
from biblioteca import *

class TestBiblioteca(unittest.TestCase):
    def test_agrega_a_lista(self):
        libro1 = Libro("Libro", "Marquez", 1930, "drama")
        usuario1 = Usuario("Agus")
        usuario1.prestar_material(libro1)
        aux = len(usuario1.materiales_prestados)
        self.assertEqual(aux,1)

if __name__ == "__main__":
    unittest.main(verbosity=2)