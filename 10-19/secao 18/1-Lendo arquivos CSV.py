"""
CSV

-Arquivos JSV sao basicamente arquivos que sao cheio de dados e
eles sao separados por ',' ';' ou por espaco

ex:
Marcio, Vitor, Vinicius, Roberta
Marcio; Vitor; Vinicius; Roberta

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)#pular a primeira linha, no caso o cabecalho
    for linha in leitor_csv:
        #cada linha e uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centimetros')

#Neste outro exemplo, usando o DictReader, nao precisa usar o next para pular o 
#cabecalho, pois ele usa o cabecalho como os valores que estao no cabecalho
#no dicionario
        
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #cada linha e uma lista
        print(f'{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} centimetros')
"""
