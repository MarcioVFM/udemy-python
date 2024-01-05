"""
POO - Herança

class cliente:

    def __initi__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome 
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}')

class funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}')

#No proximo exemplo, exitem entidades genericas que se repetem e que podem 
#ser feitas de maneiras melhores ao inves de so repetir o codigo,
#fazendo uma classe generica o suficiente que atribua a quem precise

#Ai e criada uma classe que e feita para outras classes herdarem ela
#No proximo exemplo, e a classe Pessoa que herdara para as outras
#Ela tem varios nomes, como superclasse, mae, pai, base, generica

#As classes que herdam dela sao chamadas de subclaase, filha, especifica
"""

class Pessoa:
#superclasse
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return (f'{self.__nome} {self.__sobrenome}')

class Cliente(Pessoa):
#herdou a classe Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
#herdou a classe Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

cliente1 = Cliente('Vinicius', 'Ailton', '123456789012', 2)
funcionario1 = Funcionario('Breno', 'Augusto', 98765432100, 12345)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


