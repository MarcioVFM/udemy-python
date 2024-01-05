"""
Decoretors - Decoradores

- Decorators sao funcoes
- Decorators envolvem outras funcoes e aprimoram seus comportamentos
- Ele tem a funcao de fazer uma derocacao na funcao, aprimora-la
- Tambem sao exemplo de Higher Order Functions
- Decoretors tem uma sintaxe propria, usando "@" (Syntact Sugar/Acucar Sintatico)

#Nao recomendadas, sem o @
def saudacao(definicao):
    def bom_dia():
        print('Bom dia meu querido')
        definicao()
        print('Que tenha tudo de bom para voce')
    return bom_dia

def david():
    print('Sapo cego')

saudacao_decorada = saudacao(david)
saudacao_decorada()
"""
#Com o @
def msg_auto(decorator):
    def mensagem():
        print("Ola, bem vindo a loja!")
        decorator()
        print("Oque voce deseja?")
    return mensagem

@msg_auto
def educado():
    print("Aqui voce e sempre bem vindo")

educado()
