"""
random

-Primeira coisa e que quando trablhamos com modulos, temos que 
entender que temos que importa eles, com o import, algumas
bibliotecas tem no proprio python e outras tem que ser baixadas

-Podemos importar a biblioteca inteiram porem nao e recomendado 
pois ela fica salva na memoria e elas sao muito grandes
ex: import random

-Porem podemos importaruma funcao especifica da biblioteca para 
deixar menos pesado
ex: from random import choice

-Funções importantes do random:
"""
#random: pega um numero pseudo aleatorio entre 0 e 1
from random import random
print(random())

#uniform: gera um numero aleatorio entre os limites que voce quiser
from random import uniform
print(uniform(2, 6))

#randint: gera um valor aleatorio inteiro entre os limites que voce quiser
from random import randint
print(randint(2,6))

#choice: escolhe um valor aleatorio do interavel
from random import choice
aleatorio = ['pedra', 'papel', 'tesoura']
print(choice(aleatorio))

#shuffle: embaralha um iteravel
from random import shuffle
lista = ['1', 'pao', 'queijo', '0']
shuffle(lista)
print(lista)