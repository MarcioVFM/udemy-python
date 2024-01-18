"""
Escrevendo em arquivos CSV



"""

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['titulo', 'genero', 'duracao'])
    while filme != 'sair':
        filme = input('Qual o nome do filme? ')
        if filme != 'sair':
            genero = input('Qual o genero do filme? ')
            duracao = input('qual a duracao do filme? ')
            escritor_csv.writerow([filme, genero, duracao])