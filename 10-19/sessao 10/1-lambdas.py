"""
Função lambda

-É uma função sem nome, ou função anonima

#Função em python
def função(x):
    return 3 * x + 1
print(função(3))
print(função(3))

#Expressao Lambda
lambda x: 3 * x + 1

#Forma nao usual/digna de usar o lambda
#Como utilizar a espressao lambda
calculo = lambda x : 3 * x + 1
print(calculo(3))

#Lambda com multiplas entradas
#O .title deixa a inicial maiuscula
#O .strip tira o espaço entre as palavras
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' '+ sobrenome.strip().title()
print(nome_completo('marcio', 'vinicius'))

#sem nenhuma entrada
amor = lambda: 'Como nao amar python'
print(amor())

#Maneira certa de usar o lambda
#Nesse exemplo, sera organizado o nome das pessoas de acordo com o seu sobrenome
nomes = ['Marcio Vinicius', 'Daniel da Silva', 'Vinicius Nascimento', 'Saimon Macambira', 'Breno Augusto', "Lucas Nogueira"]
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
print(nomes)

#Outra
def funçao_quadratica(a, b, c):
    return lambda x: a * x **2 + b * x + c
print(funçao_quadratica(1, 2, 3)(2))
#ou
calculo = funçao_quadratica(1, 2, 3)
print(calculo(2))
"""
