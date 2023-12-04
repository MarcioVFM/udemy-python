
'''
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G' ,'e' ,'e' ,'k', ' ','U' ,'n' ,'i' ,'v' ,'e' ,'r' ,'s' ,'i' ,'t' ,'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista6 = ['Programação', 'em', 'python:', 'Essencial']
#ex 1
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

frase = ''
for letra in lista2:
    print(letra)
    frase = frase + letra
print(frase)

#ex2: while
carrinho = []
produto = ''
while produto != 'sair':
    produto = input("adicione um produto a lista ou digite 'sair' ára sair: ")
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto, end = ', ' )
    
---------------------------------------------------------------------------------------------

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1 

#gerando o indice em for
for indice, cor in enumerate(cores):
    print(indice, cor)
  
    
'''


