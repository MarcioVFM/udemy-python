import unittest

from atividades import comer, dormir, eh_engracado

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
        )

    def test_comer_mal(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(10),
        )

    def test_eh_engracada(self):
        self.assertFalse(eh_engracado('Vinicius'))
        self.assertTrue(eh_engracado('Breno Tesoureiro'))
        self.assertTrue(eh_engracado('Roberta do Mal'))
        #self.assertFalse(None)

if __name__ == '__main__':
    unittest.main() 