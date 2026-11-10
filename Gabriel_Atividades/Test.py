import RPG as rpg 
import unittest
import matematica as mat


class Testes(unittest.TestCase):
    def test_nome(self):
        personagem = rpg.RPG("Clerson", 2, 5)
        self.assertEqual(personagem.getNome(), "Clerson")
    def test_soma(self):
        self.assertEqual(mat.Soma(3,3), 6)
        self.assertEqual(mat.Sub(5, 2), 3)
        self.assertEqual(mat.Div(3, 3), 1)
        self.assertEqual(mat.Mult(1, 5), 5)

unittest.main(argv = [''], exit=False)
