"""
Funções com parametros:

-Parametros sao valores que entram junto com as definições que fazemos
-Existem parametro e argumentos

-Parametros são variaveis que sao declaradas na definilçai de una função
-Argumentos são dados passados durante a execução de uma funçao

-Quando fazemos uma funçao com parametro, se ela na tiver o numero de 
argumentos igual ao de parametros dara keyerror

#Alguns exemplos de funçoes com parametros

#1
def quadrado(numero):
    return numero ** 2
print(quadrado(6))

#2
nome = 'Pedro'
def parabens(aniversariante):
    print(f'Parabens para o {aniversariante}!')

parabens(nome)

#
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total
lista = [1,3,3,5,7]
print(soma_impares(lista))

"""


