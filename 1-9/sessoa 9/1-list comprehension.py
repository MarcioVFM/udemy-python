"""
List comprehension

-É fazer uma nova lista com dados de uma lista
já existente

-Sintaxe
[ dado for dado in iteravel ]

#ex1
numeros = [1, 2, 3, 4]
decimal = [numero * 10 for numero in numeros]
print(decimal)

#ex2
pao = 'pao'
numeros = [1, 2, 3, 4]
paes = [f'{numero} pao' for numero in numeros]
print(paes)

#3
print([numero * 3 for numero in range(1, 10)])

#4
print([ bool(valor) for valor in [0, [], '', 1, 3, True]])

#5 
print([str(numero) for numero in range (1, 10) ])

===================================================================
 PARTE 2
Utilizando estruturas condicionais

#1
lista = [1, 2, 3, 4, 5]
par = [numero for numero in lista if numero % 2 == 0 ]
impar = [numero for numero in lista if numero % 2 != 0]
print(par, impar)

#2
lista = [1, 2, 3, 4, 5, 6]
calculo = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lista ]
print(calculo)

#2
lista = [1, 2, 3, 4, 5, 6]
calculo = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lista ]
print(calculo)
"""
