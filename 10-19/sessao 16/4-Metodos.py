"""
POO - Metodos(def):

--Metodos (funcoes): Representam os comportamentos do objeto. Ou seja, as acoes 
que esta objeto pode realiar no seu sistema.

--Em Python dividimos os metodos em 2 grupos: Metodos de Instancia e 
Metodos de Classe

--Metodos sao escrito em letra minusculos e separados por _

OBS: Nao e aconselhado a criacao def funcoes dunder (__.__), a linguagem python
possue varios metodos com esse tipo de nomeclatura e pode ser e seja mudado seu 
comportamento

--Metodos de Instancia
    Sao metodos que estao dentro ca classe

 O metodos __init__ e um metodosespecial chamado de contrutor e
 sao funcao e construir o objeto a partir da classe

--Metodos de Classe

from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 10000

    def __init__(self, limite, saldo):
        self.__id = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__id


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome= nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
           #Retorna o valor do produto com desconto
        return self.__valor * (100 - porcentagem) / 100



class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
    
    def nome_completo(self):
           #Retorna o nome completo do usuario
        return self.__nome + ' ' + self.__sobrenome
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

p1 = Produto("PS5", "Console", 4000)
print(p1.desconto(20))

u1 = Usuario('Marcio', 'Vinicius', 'marciov85@gmail.com', '12345')
print(u1.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('informe o sobrenome:')
email = input('informe o seu email: ')
senha = input('informe sua senha: ')
confirma_senha = input('confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)

else:
    print('A senha nao e a mesma')
    exit(1)

print('Usuario criado com sucesso')
senha = input('Informe a sennha para acesso: ')

if user.checa_senha(senha):
    print('acesso permitido')

else:
    print('acesso negado')

print(f'Senha do usuario criptografada {user._Usuario__senha}')
"""
from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 10000

    def __init__(self, limite, saldo):
        self.__id = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__id


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome= nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
            #Retorna o valor do produto com desconto
        return self.__valor * (100 - porcentagem) / 100



class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
    
    def nome_completo(self):
           #Retorna o nome completo do usuario
        return self.__nome + ' ' + self.__sobrenome
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

p1 = Produto("PS5", "Console", 4000)
print(p1.desconto(20))

u1 = Usuario('Marcio', 'Vinicius', 'marciov85@gmail.com', '12345')
print(u1.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('informe o sobrenome:')
email = input('informe o seu email: ')
senha = input('informe sua senha: ')
confirma_senha = input('confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)

else:
    print('A senha nao e a mesma')
    exit(1)

print('Usuario criado com sucesso')
senha = input('Informe a sennha para acesso: ')

if user.checa_senha(senha):
    print('acesso permitido')

else:
    print('acesso negado')

print(f'Senha do usuario criptografada {user._Usuario__senha}')




