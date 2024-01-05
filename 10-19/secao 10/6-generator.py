"""
Generator 

-Tem a mesma ideia do list comprehension,porem é em formato de tupple,
entretanto funciona que nem maps e filter, quando voce usa ele é apagado da memoria
-Sua vantagem e que ele consome um espaço minimo na memoria, diferente do list, dic e set
comprehesion


#list comprehension
nomes = ['Carlos', 'Camila', 'Caio', 'David']
res = (any([nome[0] == 'C' for nome in nomes]))#list
print(res)
#nomec = list(filter(lambda nome: nome[0] == 'C', nomes))
#print(nomec)

#Generator
res2 = (any(nome[0] == 'C' for nome in nomes))
print(type(res2))
print(res2)
"""
