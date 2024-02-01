import unittest

from robo import Robo

class RoboTestes(unittest.TestCase):

    def setUp(self):
        #o metodo setUp ele sempre sera rodado em todas as def
        self.megaman = Robo('megaman', bateria=50)

    def teste_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def teste_dizer_nome(self):
        self.megaman.dizer_nome()
        self.assertEqual(self.megaman.bateria,49)
        self.assertEqual(self.megaman.dizer_nome(), 'EU SOU MEGAMAN')

    def tearDown(self):
        print('O tierDown esta sendo executado')
if __name__ == '__main__':
    unittest.main()