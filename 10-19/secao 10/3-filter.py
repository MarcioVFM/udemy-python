""""
Filter

-Serve para filtrar oque voce quer de uma lista
-Funciona igual ao maps, exclui seu dado apos o uso

#Biblioteca para trabaçhar com dados estatisticos
import statistics
lista = [1, 2, 3, 4, 5, 6]
media = statistics.mean(lista)
#media = sum(lista) / len(lista)
print(media)
print(list(filter(lambda x: x > media, lista)))


#Fazer um filtro que tire os espaços em branco da lista
paises = ['Brasil', 'Argentina', 'Peru', '', ' Chile', '', '', 'Venezuela']
filtrado = filter(None, paises)
#Melhor maneira, quando nao tem nada na area da lista, ele retorna None ou False
#Outras maneiras menos eficazes
filtrado2= filter(lambda paises: paises != '')
filtrador3 = filter(lambda paises: len(paises) > 0)


#Fazer um filtro que veja um usuario e seus tweets, e filtre os usuarios que nao twetaram nada
usuarios = [
    {'usuario':'David Rocha', 'tweets':[]},
    {'usauario':'Daniel da Silva', 'tweets':['Jogo de masteryi','Comi o cu de qm ta lendo']},
    {'usauario':'Vinicius do Nascimento', 'tweets':[]},
    {'usauario':'Marcio Vinicius', 'tweets':['Ama as pessoas', 'Pixelart fodase']},
    {'usauario':'Vitinho o Hugo', 'tweets':['Malhar malhar']},
]
#print(usuarios)
#forma1, melhor
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
#forma 2
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))


#Pegar o nome das professoras de uma lista e criar uma outra lista
#colocando 'Minha professora e a {nome}', somente com os nomes com menos de 5 caracteres
nomes = ['Vanessa', 'Paulo', 'Ana', 'Iso']
frase = list(map(lambda nome: f'Minha professor(a) é a {nome}' ,filter(lambda nome: len(nome) < 5, nomes)))
print(frase)
"""
