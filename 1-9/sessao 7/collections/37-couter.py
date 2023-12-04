"""
-Couter
-Ele conta quantas vezes aquele valor foi repetido na lista, e depois ele cria algo semlhante
a um dicionario para representar o valor e a quantidade de vezes que foi repetido


"""
from collections import Counter
lista = [1, 1, 1, 1, 1, 2, 2, 3, 3, 55, 55, 55, 55, 123123, 77, 77]
coleção = Counter(lista)
print(coleção)