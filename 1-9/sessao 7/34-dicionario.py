"""
#Dicionario
#Se usa chaves para representar ele {}
#Server para colocar um outro tipo de valor ou nome no indice dos objetos que estão na variavel
Ex: localc = {'40': casa1, '20':casa2, '34':casa3} 
#Sendo o valor que esta no '' o numero do indice e depois do : o que foi atribuido no dicionario

#Como achar um valor pelo indice? .get, pois se nao tiver o indice certo não ira dar Keyerror
print(localc.get(40)) \\ casa1

casa = localc.get('10', 'Nao encontrei o número dessa casa') \\ Caso nao encontre o valor no dicionario, será atribuido o outro valor com o .get, não dará Keyerror
print(localc)

#Como adicionar um valor no dicionario
localc['50'] = 'casa4'

#Como atualizar um valor no dicionario
novacasa = {'30':'casa5'}
localc.update(novacasa) #ou tambem pode ser feito assim: localc.update({'30':'casa5'})

#Remover dado
localc.pop('30')

#Mostrar somente o indice
for indice in localc.keys():
    print(indice, end= ', ')

#Mostrar somente os valores
for valores in localc.values():
    print(valores, end= ', ')

"""
