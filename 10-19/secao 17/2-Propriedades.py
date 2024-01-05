"""
POO - Propriedades - Propeties

- Esses modulos sao conhecidos por getters e setters, onde os
 getters retornam o valor do atributo e o setters alteram o 
 valor do mesmo

"""

class Conta:

        contador = 0

        def __init__(self, titular, saldo, limite):
                self.__numero = Conta.contador + 1
                self.__titular = titular
                self.__saldo = saldo
                self.__limite = limite
                Conta.contador =+ 1
        
        #O property faz com que voce tenha o acesso correto aos atributos
        @property
        def titular(self):
                return self.__titular
        
        @property
        def limite(self):
                return self.__limite
        
        @property
        def saldo(self):
                return self.__saldo
        
        #O setter muda o valor do atributo, tem que ser cuidadoso com os setters
        @limite.setter
        def limite(self, novo_limite):
                self.__limite = novo_limite

        def extrato(self):
               return f'Saldo de {self.__saldo} do cliente {self.__titular}'

        def depositar(self, valor):
                self.__saldo += valor

        def sacar(self, valor):
                self.__saldo -= valor 
            
        def transferir(self, valor, destino):
                self.__saldo -= valor
                destino.__saldo += valor



conta1 = Conta('Breno', 1000, 500)
conta2 = Conta('Daniel', 1200, 400)

conta1.limite = 700
print(conta1.titular)

