"""
Funcoes de maior grandeza - Higher Order Functions - HOF

-Quando uma linguagem de programacao suporta HOF, significa que podemos
ter funcoes que retornam outras funcoes como resuldado ou que podemos 
passar funcoes como arguemntos para outras funcoes, e ate mesmo criara 
variaveis do tipo de fguncoes do nossos programas

-Utilzamos isso na secao de funcoes.

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def calcular(num1, num2, definicao):
    return definicao(num1, num2)

print(somar(1, 1))

#Nested Functions - Funcoes Aninhadas
#Em python podemos tambem ter funcoen dentro de funcoes,
#essas sao as funcoes aninhadas

"""
from random import choice
def comprimento(pessoa):
    def humor():
        return choice(('Ola, Bom dia ', 'Vai tomar no cu o ', 'Bao uai sô'))
    return humor() + pessoa    
print(comprimento('David'))