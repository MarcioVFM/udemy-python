"""
Preservando metadatas com Wraps

-Oque sao metadados? Sao dados intrisecos em arquivos

-Wraps: Sao funcoes que envolvem elementos com diversas finalidades
#Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
          #Eu sou uma funcao logar dentro de outra
        print(f'Voce esta chamando {funcao.__name__}')#Pega o nome do def
        print( f'Aqui a documentaca: {funcao.__doc__}')#Pega as anotacoes nos "
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
       #Soma dois numeros
    return a + b

print(soma(1, 2))
print(soma.__name__)#Desse jeito, ele vai pegar os metadados de ver_log
print(soma.__doc__)#Mesma coisa ^, acontece por conta do decoretor, o @
"""
#Resolucaso, so adicionar o @wraps na primeira funcao
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funcao logar dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')#Pega o nome do def
        print( f'Aqui a documentaca: {funcao.__doc__}')#Pega as anotacoes nos "
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b

print(soma(1, 2))
print(soma.__name__)
print(soma.__doc__)



