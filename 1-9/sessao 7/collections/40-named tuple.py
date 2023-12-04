'''
Named Tuple
-Basicamente faz a tupla igual um dicionario, mas ainda continua com a função de
tupla de ser imutavel com algumas novas funções
'''
from collections import namedtuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])
ray = cachorro (idade=2, raca='chowchow', nome='ray')
print(ray)
