"""
Maps

-Maps e uma ferramenta para facilitar no uso das funçoes com listas
-Sintaxe: maps(função, lista)
#ex
import math 

lista = [1, 2, 3, 4, 5]
def area(r):
    return math.pi * (r ** 2) 
areas = map(area, lista)
print(areas)
print(list(areas))
print(areas)

-Depois que voce converte o map para lista uma vez, ele se apaga da memoria

#Com lambda
import math
lista = [1, 2, 3, 4, 5]
print(list(map(lambda x: math.pi * (x ** 2), lista)))

#Com lambda
import math
lista = [1, 2, 3, 4, 5]
print(list(map(lambda x: math.pi * (x ** 2), lista)))

#Outro ex
temperatura_cidades = [('Manaus', 35), ('Curitiba', 15), ('São Paulo', 29), ('Rio de Janeiro', 32)]
f_p_c = lambda dado: (dado[0], 32 + dado[1] * 9 / 5 )
print(list(map(f_p_c, temperatura_cidades)))
#Utilizando certo o lambda
temperatura_cidades = [('Manaus', 35), ('Curitiba', 15), ('São Paulo', 29), ('Rio de Janeiro', 32)]
print(list(map(lambda dado: (dado[0], 32 + dado[1] * 9 / 5 ), temperatura_cidades)))
"""


