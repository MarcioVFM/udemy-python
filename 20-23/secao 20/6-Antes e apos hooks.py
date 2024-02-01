"""
Unittest - Antes e apos os Hooks

Hooks - Sao os testes em si

setup() - É executado antes antes de cada metodo de teste, e util para criamos instancias de objetos e outros dados;


tearDown - e executado ao fgianl de cada metodo de teste. É util para excluir dados ou fechar conexoes com bannco de dados



"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        #configuracoes do setUp
        pass

    def test_primeiro(self):
        #setUp vai rodas antes do teste
        #o tearDown() vai rodas apos o teste
        pass
    
    def tearDown():
        pass
