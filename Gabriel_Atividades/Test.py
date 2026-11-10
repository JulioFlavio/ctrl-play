import RPG as rpg 
import unittest

class Testes(unittest.TestCase):
    personagem = rpg.RPG("Clerson", 2, 5)

    def test_nome(self):
        self.assertEqual(personagem.getNome(), "Clerson")

unittest.main(argv = [''], exit=False)
