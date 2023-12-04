"""
Bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o aquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with e utilizado para criara um contexto de 
trabalho onde os recursos sao fechados apos o bloco with

arquivo = open('teste/texto.txt')

"""

with open('teste/texto.txt') as arquivo:
    print(arquivo.readlines())
print(arquivo.read())