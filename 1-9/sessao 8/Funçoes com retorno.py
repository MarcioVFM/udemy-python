""""
Funções com retorno

-São funções que retornam um valor quando sao usadas, ex:.pop 
-O mais comum a ser usado e o return
-O return ele encerra a função em que ele esta e retorna um numero
-Se tem algo abaixo do return ele e ignorado
Ex:
def quadrado_de_7():
    return 7 * 7
print(quadrado_de_7())
 
-A principal diferença entre usar o print() e o return e que 
pode manipular o valor no return, e o o print nao
Ex1:
Print():
def quadrado_de_7():
    print(7 * 7)
print(quadrado_de_7() + 2 ) #TypeError

Return:
def quadrado_de_7():
    return 7 * 7
print(quadrado_de_7() + 2 )

Ex2:
nome = ' pedro'
def oi():
   return 'oi'
print(oi() + nome)


-Mais de um return em uma função
def retorno():
   print('estou sendo executado')
   return
   print('nao estou sendo executado')
 

-Exemplo de return: Cara ou coroa com import do random, que e uma
coleção que pega um numero aleatorio entre 0 e 1

from random import random
def moeda():
    if random() > 0.5:
       return 'cara'
    return 'coroa'
print(moeda())


-Como usar sua def em outra aba
def test():
   return 'teste'
#em outra aba
from nome_da_pasta import test()
"""



