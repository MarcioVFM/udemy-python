"""
**kwargs
-Funcionam parecido com o *args, a diferença é que eles não são tuplas,
mas sim dicionários
-Não são obrigatorios

#ex1:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita do {pessoa} é {cor}')
cores_favoritas(Pedro='azul', Roberta='roxo', Henrique='verde')

-Tem uma ordem a ser executada uma função, essa ordem é:
- 1: Parâmetros obrigatórios
- 2: *args
- 3: Parâmetros não obrigatórios
- 4: **kwargs

def minha_função(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade}')
    print(args)
    if solteiro:
        print(f'{nome} e um homem casado')
    else:
        print(f'{nome} está procurando casadas')
    print(kwargs)
minha_função(22, 'Marcio', 'amavel', cor='roxo' )


-Desempacotar **kwargs
-Tem uma maneira simples em python que e somente colocar o dicionario na 
execução e colocar **
-So finciona se o valor dos indices do dicionarioforem iguais aos parâmetros
da função


def desempacotar(**kwargs):
    return f"{kwargs['nome']}, {kwargs['sobrenome']}"
nomes = {'nome': 'Marcio', 'sobrenome': 'Vinicius'}
print(desempacotar(**nomes))

"""




