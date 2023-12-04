'''
Orderer Dict
-É uma collections que faz com que a ordem dos elementos do dicionario seja algo 
relevânte

'''
from collections import OrderedDict
dicionario1 = {1:'a', 2:'b'}
dicionario2 = {2:'b', 1:'a'}
print( dicionario1==dicionario2)
dicionario1 = OrderedDict({1:'a', 2:'b'})
dicionario2 = OrderedDict({2:'b', 1:'a'})
print(dicionario1==dicionario2)