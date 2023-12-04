'''
min(), max()

Basicamente para achar o maior ou o menor valor de um iteravel
de dois ou mais elementos

#ex:
lista = [1, 4, 3, 21431234, 7]
print(max(lista)) #21431234
print(min(lista)) #1

#ex com dicionario:
dicionario = {'a': 1, 'b':2, 'c':3}
print(max(dicionario)) #a
#para pegar o indice
print(max(dicionario.values()))


#Uma lista com varios nomes, se voce usar o max, ele pegara o
nome com a primeira letra maior no alfabeto, mas tem como ver 
pelo tamanho do nome
nomes = ['Marcio', 'Julia', 'Matheus', 'Fernanda']
print(max(nomes)) #Marcio
print(max(nomes, key=lambda nome: len(nome))) #Fernanda

#mostrar a musica que foi mais tocada ou menos tocada
musicas = [
    {"titulo": "Churrasquinho", "tocou": 50},
    {"titulo": "Pericles", "tocou":49},
    {"titulo": "Pixote", "tocou":22},
]
print(musicas)
print(max(musicas, key=lambda musica: musica["tocou"]))

#mostrar so o titulo da musica mais tocada
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
'''