import atividad as atv
import unittest

class Testes(unittest.TestCase):
    def test_nome(self):
        p = atv.personagem("iaiaaaia", 200, 500)
        self.assertEqual(p.getNome(), "iaiaaaia")

unittest.main(argv=[''], exit=False)
