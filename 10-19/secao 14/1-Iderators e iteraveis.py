"""
Entendendo Iteratos e itarables
--resumo--
iterator retorna um dado por vez, com a função next()
iterable retorna tudo de uma vez

iterator:
    - E um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma funçao next()
    é chamada

Iterable:
    - Um objeto que ira retornar um iterator quando a função inter() for chamada


nome = "pedro" #É um iterable mas nao e um iterator
numero = [1, 2, 3, 4, 5, 6]#É um iterable mas nao e um iterator

print(next(nome)) #str error
"""
nome = "pedro" #É um iterable mas nao e um iterator
numero = [1, 2, 3, 4, 5, 6]#É um iterable mas nao e um iterator

it1 = iter(nome)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))






