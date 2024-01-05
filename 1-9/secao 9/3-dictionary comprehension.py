'''

importante: Dicionario nao pode ter indices iguais

#1
dicionario = {'a':1, 'b':2, 'c':3, 'd': 4, 'e':5}
print(dicionario)
quadrado = {indice:valor ** 2 for indice, valor in dicionario.items}
print(quadrado)

#2
lista = [1, 2, 3, 4, 5]
quadrado = {numero:numero ** 2 for numero in lista}
print(quadrado)

#3
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range (5)}
print(mistura)
'''

#4 Exemplo com logica condicional
numeros = [1, 2, 3, 4, 5]
tipo = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(tipo)