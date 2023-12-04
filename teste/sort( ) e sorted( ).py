"""
O sorted ele nao modifica a lista
o sort modifica a lista
"""

lista = [2, 3, 6, 1]
print(sorted(lista))
print(lista)

lista2 = [3, 5, 8, 2]
lista2.sort()
print(lista2)