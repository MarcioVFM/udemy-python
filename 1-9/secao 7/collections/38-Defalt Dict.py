"""
Defalt Dict

-É usado nos dicionarios, quando procura um indice e nao tem no dicionario, ao inves de dar
KeyError, ele adiciona aquele indice a ele e coloca um valor nele
-lambda: São funções que podem ou não receber parâmetro de entrada e retornar valores \\nao foi estudado ainda
"""
from collections import defaultdict
dicionario = defaultdict(lambda:0)
dicionario['teste'] = 'chave'
print(dicionario)
print(dicionario['indice'])
print(dicionario)