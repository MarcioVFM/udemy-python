"""
Polimorfismo

Poli - Muitas
Morfis - Formas

-E basicamente a questao de sobreescrever um metodo de uma classe
mae, como e intecional esse polimorfismo no falar, que caso ele
nao seja sobreescrito, dara um error
-
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def falar(self):
        raise NotImplementedError ('A classe filha precisa implementar este metodo')
    
    def comer(self):
        print(f'{self.__nome} esta comendo ')

class Cachorro(Animal):

    def __iit__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal.__nome} fala auau')

class Gato(Animal):

    def __init__ (self, nome):
        super().__init__(nome)


