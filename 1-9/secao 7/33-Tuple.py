'''
Tuple ou tuplas

Diferenças de tuplas e listas #Tuplas sao mais seguras que listas
                              #Tuplas sao mais rapidas que listas

1- São representadas por parenteses ()

2- - As tuplas são imutaveis: Isso signigica que ao se crar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

#Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1= (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#Cuidado 2: Tuplas com 1 elementos

tupla3 = (3)#Pra python, isso nao e uma tupla
print(type(tupla3))

tupla4 = (4,)
print(type(tupla4))
#A tupla e definida pela vírgula

#Podemos criar uma tupla dinamicamente
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desempacotamento de tupla
tupla = ('Geek University', 'Programação em python')
escola, curso = tupla
print(escola)
print(curso)
#Gera value erro se colocarmos um numero diferente de elementos para desempacotar

#Contatenação de tuplas
tupla1 = 1, 2, 3
tupla2 = 4, 5, 6
 print(tupla1 + tupla2)

 #Verificar se determinado elemento esta na tupla
tupla1= 1, 2, 3
print(3 in tupla1)
print(23 in tupla1)

#|Iterando sobre tupla
tupla1= 1, 2, 3
for i in tupla1:
    print(i)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

#Na tupla nao temos problema com shallow copy    
 '''

