""""
POO - Objetos

Objetos -> Sao instancias da classe. Ou seja , apos o mapeamento do 
objeto do mundo real para sua representação computacional, devemos
poder criar quantos objetos forem necessarios. Podemos pensar nos 
objetos/instancias de uma classe como variaveis do tipo definido na 
classe

#Isntacia/Objetos
lamp1 = Lampada('Branco', 110, 60)
lamp1.ligar_desligar()#liga a lampada
print(f'A lampada esta ligada? {lamp1.checa_lamp()}')#verifica se a lampada ta ligada ou desligada
"""
class Lampada:

    def __init__(self, cor, luminosidade, voltagem):
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__voltagem = voltagem
        self.__ligada = False
    
    def checa_lamp(self):
        return self.__ligada
    
    def ligar_desligar (self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
    
class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    def nome_return(self):
        return self.__nome

class ContaCorrente:

    def __init__(self, limite, saldo, cliente):
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
    
    def nome_cliente(self):
        print(f'O nome do cliente é {self.__cliente.nome_return()}')


cliente1 = Cliente('Marcio', 123123)

cc1 = ContaCorrente(100, 500, cliente1)

cc1.nome_cliente()


