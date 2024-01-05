"""
Decoretors com diferentes Assinaturas

#Para resolver, utlizamos um padrao de projeto chamado Decoretor Pattern

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(b):
    return f'Ola, eu sou a/o `{b}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}'

#teste
print(saudacao('Paula'))

print(ordenar('Picanha', 'batata frita')) 
#Dara TypError pois tem mais uma variavel sendo enviada

#-----Utilizando o *args e **kwargs--------
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(b):
    return f'Ola, eu sou a/o `{b}'

@gritar
def ordenar(principal, acompanhamento, sobremesa):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, de sobremesa quero {sobremesa}'

print(saudacao('Paula'))

print(ordenar('Picanha', 'batata frita', 'pudim'))
"""

#-------Decoretors com argumentos--------

def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verificar_primeiro_argumento('hotdog')
def comida_favorita(*args):
    print(args)

print(comida_favorita('hamburguer', 'hotdog'))#Ira mandar a mensagem de erro, pois o primeiro arguemnto nao e hotdog