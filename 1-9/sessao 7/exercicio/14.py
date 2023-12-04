lista = [1,1,1,2,5,1,2,6]
print(lista)
def remove_dups_fromkeys(lista):
    return list(dict.fromkeys(lista))
lista = remove_dups_fromkeys(lista)
print(lista)