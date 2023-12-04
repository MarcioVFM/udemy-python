"""
__main__ e __name__

-Server para que quando voce tiver importanto um arquivo,
a parte que tiver o main nao seja realizada, so ira ser executado 
no main quando voce executar aquele arquivo em especifico, e oque 
tiver fora do main sera executado no import

"""
lista = [1, 2, 3, 4, 5, 6]
soma = lambda lista: sum(filter(lambda a: a%2 != 0, lista))
resultado = soma(lista)
print(resultado)
print(resultado)
