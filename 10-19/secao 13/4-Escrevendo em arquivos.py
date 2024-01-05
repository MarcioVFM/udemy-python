"""
Escrevendo em arquivos

-Quando escrevemos em um arquivo, se ele nao existir,
sera criado um novo, se ele ja existir, oque estiver
escrito nele sera apagado
-Para escrever em um arquivo, apos a sua abertura e 
necessario utilizar a função write(), essa funcao 
recebe uma string como parametro, caso o contrario
sera dado TypeError

with open('escrita.arquivo', "w") as arquivo:
    arquivo.write('Escrevendo algo\n')
    arquivo.write('escrevendo ainda mais coisa')
"""

with open('escrita.arquivo', "w") as frutas:
    while True:
        fruta = input('Escreva nomes de frutas, caso queira sair, digite: ')
        if fruta != 'sair':
            frutas.write(fruta)
            frutas.write("\n")
        else:
            break
