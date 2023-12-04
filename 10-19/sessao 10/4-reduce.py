"""
Reduce

-E uma funcao, que recebe uma funcao e uma lista, e essa funcao pode 
so receber 2 numeros
-E preferivel usar o loopfor pois e mais facil de entender, porem
se voce que demostrar seu conhecimento de python, use reduce
-como usar:
recuce(funcao, lista)
ex:

lista = [1, 2, 3, 4, 5, 6]
#usando reduce
from functools import reduce
funcao = lambda x, y: x * y
res = reduce(funcao, lista)
print(res)

#usando loop
n = 1
for x in lista:
    res = res * n
"""
