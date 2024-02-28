"""
type hinting

basicamente para definir o tipo de dado que voce quer
seja e que retorne o objeto

def cumprimentar(nome:str) -> str:#so ira funcionar se for uma str
    return f"ola {nome}"

nome1 = input('Qual o seu nome?: ')
print(cumprimentar(nome1))

"""

def cabecalho(titulo: str, alinhamento: bool =True) -> str:
    if alinhamento:
        print(f"{titulo.title()}\n{ '-' * len(titulo)}")
    else:
        print(f" {titulo.title()} ".center(50, '#'))
              
cabecalho('marcio vinicius')
cabecalho('roberta gabi', alinhamento = False)#aqui, podemos executar o alinhamento com uma variavel sem ser boolean

"""
Para achar esse problema na questao do booleano na def cabecalho, podemos usar um mypy,
uma ferramenta que trabalha junto com o tipinghint para verificar oque esta sendo
executado de forma erronea 
"""