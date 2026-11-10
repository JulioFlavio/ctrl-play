import RPG as rpg 
import unittest

class Testes(unittest.TestCase):
    def test_nome(self):
        personagem = rpg.RPG("Clerson", 2, 5)
        self.assertEqual(personagem.getNome(), "Clerson")

unittest.main(argv = [''], exit=False)
