"""
POO- Abstracao e Encapsulamento

-O grande objetovo da POO e encapsular o nosso codigo dentro 
de um grupo logico e hierarquico utilizando classes

encapsular -> capsula  

        classe
''''''''''''''''''''''
/                    /
/  atributos/metodos /
/                    /
''''''''''''''''''''''

-Abstracao: Em POO, e o ato de expor apenas dados relevantes 
de uma classe, escondendo atributos e metodos privados 
de usuario
"""

class Conta:

    contador = 1000

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    def extrato(self):
        print(f'O saldo da conta do(a) {self.__titular} é de {self.__saldo}, e seu limite disponivel e de {self.__limite} ')

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo indisponivel')
        else:
            self.__saldo -= valor
            print(f'Saldo disponivel: {self.__saldo}')
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Novos saldo de {self.__saldo}')
        else:
            print('O valor precisa ser positivo')
    
    def transferencia(self, valor, conta_destino):
        if self.__saldo > valor:
            self.__saldo -= valor
            conta_destino.__saldo += valor 
            print(f'Tranferencia de {valor} realizada para {conta_destino.__titular}')
        else:
            print('saldo indisponivel')

conta1 = Conta('Marcio', 1000, 5000)
conta2 = Conta('Silmara', 1500, 6000)
conta1.extrato()
conta1.sacar(1001)
conta1.transferencia(100, conta2)
print(Conta)

