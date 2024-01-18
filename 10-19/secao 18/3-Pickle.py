"""
Pickle

#Criando arquivo pickle
import pickle

oliver = Cachorro('Oliver')
jasmin = Gato('Jasmin')
bruce = Cachorro('Bruce')

with open('animais.pickle', 'wb') as arquivo:#wb = write binare
    pickle.dump((bruce, jasmin, oliver), arquivo)


#Abrindo arquivo pickle

with open('animais.pickle', 'rb') as arquivos:
    cachorro1, gato, cachorro2 = pickle.load(arquivos)
    print(f'O cachorro chama-se {cachorro1.nome}')
    cachorro1.latir()
    print(f'O cachorro se chama {cachorro2.nome}')
"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} esta comendo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def mia(self):
        print(f'O {self.nome} esta miando')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'O {self.nome} esta latindo')

