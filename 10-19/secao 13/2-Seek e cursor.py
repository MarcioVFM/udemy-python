"""
Seek e cursor

-Quando voce usa o aquivo.read, e voce usalo novamente nao lera nada,
isso porque o texte e lido de acordo com o cursor, quando ele e lido 
o cursor fica no final do texto e ele nao sai de la, assim temos
que usar uma função para mover ele novamente para o comecou ou outra
parte do texto

-seek(): E utilizado para movimentar o cursor pelo arquivo

arquivo = open("teste/texto.txt")
print(arquivo.read())
arquivo.seek(0)

-readline(): Faz le uma linha do arquivo

-readlines(): Faz uma lista com todas as linhas do arquivo
"""
