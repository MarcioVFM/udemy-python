"""
sorted()

É bem parecido com o .sort, bota a lista em ordem,
porem ele nao mexe na lista atual, so mexe no momento
em que ele e usado, e o .sort ele mexe em si na lista 
"""

tupla = (5, 2, 3, 4)
lista = list(sorted(tupla))
print(lista)