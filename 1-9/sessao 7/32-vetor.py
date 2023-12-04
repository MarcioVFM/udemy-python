'''
Listas 

listas em python funcionan como vetores/matrizes (arrays) 
em outras linguagens, com a diferença de
serem dinâmico e também de podermos clocar qualquer tipo de dado.

-Dinâmico:
*Em Python, eles nao tem tamanho fixo, se pode criar a lista e 
simplesmente adicionar elementos
*Elas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer
tipo de dado
 
-As listas em python sao representadas por colchetes []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G' ,'e' ,'e' ,'k', ' ','U' ,'n' ,'i' ,'v' ,'e' ,'r' ,'s' ,'i' ,'t' ,'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Checar determinado valor na lista
num = 18
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Nao encontrei o numero {num}')

#Ordenar uma lista
lista1.sort()
print(lista1)

#Podemos contar o numero de ocorrências de uma lista
print(lista1.count(1))
print(lista5.count('e'))

#Adicionar elementos em listas, utilizamos a função append
#Com append so se pode adicionar 1 elemento por vez 
print(lista1)
lista1.append(42)
print(lista1)

#Da pra colocar uma lista com append, como ele e so uma valiravel com varios elementos
#Desse jeito, vc vai adinionar outra lista dentro da lista
lista1.append([3, 6, 78])
print(lista1)

#Com o .extend voce adicinara aqueles valor a lista
#Com o .extend so pode adicionar mais de um numero, se for somente um elemento se usa .append
lista1.extend([5, 6, 22])
 print(lista1)

#tanto o .append e o .extend vao adicionar o elemento ao final da lista
#Entretando da para selecionar sua posição de uma maneira
lista1.insert(2,'novo valor')
print(lista1)

#Juntar listas
lista1.extend(lista2)
print(lista1)

#Inverter listas
lista1.reverse()
print(lista1[::-1])#outra maneira de inverter

#copiar uma lista
lista6=lista2.copy()

#saber o tamanho da lista
print(len(lista1))

#remove e retorna o ultimo elemento da lista
print(lista1.pop(2))

#copiar uma lista
lista6=lista2.copy()

#saber o tamanho da lista
print(len(lista1))

#remove e retorna o ultimo elemento da lista
print(lista1.pop(2))

#Limpar lista
lista1.clear()

#Repetir elementos de uma lista
lista2= lista2 * 3

#Converter uma string em lista
#O .split cria diferente elementos de acordo com o espaço na string
curso = 'Programação em python: essencial'
curso = curso.split()
print(curso)

#Converter uma lista em string
curso1 =' '.join(lista6)
print(curso1)

#achar o indice de um elemento na lista

print(lista1.index(1))

#da para usar o index igual range, indes.(variavel que procura, inicio, fim)
print(lista1.index(1, 2, 8))

#checando se existe o valor na lista
if 2 in lista1:
    print('existe o numero 2 na lista')
else:
    print('Nao tem o numero 2 na lista')

    #revisando o slicing 
print(lista1[1:])#comecando no 1 ate o final
print(lista1[1:4:2])#comecando do indice 1, terminando no 4, pulando de 2 em 2

#trocadno indices da lista
lista1[0], lista1[1] = lista1[1], lista1[0]
print(lista1[0], lista1[1])    

#soma, valor maximo, valor minio de uma lista
print(max(lista1))
print(min(lista1))
print(sum(lista1))

#deep copy
nova = lista1.copy()

#shallow copy

nova1 = lista1

#a diferença entre as duas e que na deep, a nova lista e
#independente da lista1, na shallow quando a nova1 ou a
#lista1 e modificada, ambas modificam
'''
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G' ,'e' ,'e' ,'k', ' ','U' ,'n' ,'i' ,'v' ,'e' ,'r' ,'s' ,'i' ,'t' ,'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista6 = ['Programação', 'em', 'python:', 'Essencial']

