"""
Loop -> Estrutura de repetição
For -> |Uma dessas estruturas

#Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10)

# Exemplo de for 1
for letra in nome:
    print(letra)

#Exemplo 2
for valor in enumerate(nome):#aqui o 'enumerate' vai colocar o numero de acordo com a localização da letra
    print(valor)

"""
qtd = int(input('quantas vezes esse loop deve rodar?'))
soma = 0 
for n in range(0, qtd):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')


