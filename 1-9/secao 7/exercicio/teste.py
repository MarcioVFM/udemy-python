"""
lista = [5, 7, 2]
indices = sorted(range(len(lista)), key=lambda i: lista[i], reverse=True)
print(indices) # [1, 0, 2]
"""

lista = [1,1,1,2,5,1,2,6]
print(lista)
def remove_dups_fromkeys(lista):
    return list(dict.fromkeys(lista))
lista = remove_dups_fromkeys(lista)
print(lista)