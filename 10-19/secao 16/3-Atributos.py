"""
Atributos

-Atributos representam as caracteristicas do objeto. Ou seja,
com atributos conseguimos representar computacionalmente 
os dados de um objeto

Em Python, dividimos os atributos em 3 grupos
    -Atributos de Instancia;
    -Atributos de Clase;
    -Atributos Dinamicos;

-Atributos de instancia:Sao atributos declarados dentro do metodo construtos

-Metodo construtor: E um metodo especial utilizado para a construcao do ojeto

-Metodo: sao funcoes dentro de uma classe (funcado = def, classe = class)

-self: ex class Lampada: self voltagem, o objeto Lampada vai receber o atributo voltagem

#Classe de instancia Publica
class Lampada:

    def __init__(self, voltagem, cor):#metodo construtor: __init__
        self.voltagem = voltagem
        self.cor = cor
        self.ligar = False

class ContaCorrente:
    
    def __init__(self, numero, descricao, valor):
        self.numero = numero
        self.descricao = descricao
        self.valor = valor

Class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        
class Usuario:

    def __init__(conta, nome, email,senha):
        conta.nome = nome
        conta.email = email
        conta.senha = senha

---Atributos publicos e privados---
-Em python, todos os atributos de uma classe é publico
-Ou seja, pode ser acessado em todo o projeto
-Caso queira transformar o atributo em privado, ou seja, ser utilizado somente dentro
da propria classe onde esta declarado, utiliza-se o __ duplo
-Isso e conhecido tambem como Name Mangling

#Classes de atributos privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    def mostra_senha(self):
        print(self.__senha)
    def mostrar_email(self):
        print(self.email)

#OBS: Isso e apenas uma conveção, ou seja, a linguagem python nao vai impedir
#que se faca acesso aos atributos sinalizados como privados fora da classe
#Python nao obriga vc a fazer uma classe privada,

user = Acesso('marciov859@gmail.com', 'amolol')
print(user.email)
#print(user.__senha)#dara erro
print(dir(user)) #dir() mostra os diretorios dos user, assim ele mostrara como acessar a senha, com o _Acesso__senha
#print(user._Acesso__senha)#Temos acesso, mas nao deveriamos fazer esse acesso
#Name Manglin: Quando colocamos privado, ele junta o nome da _clasee + atributo
 
user.mostra_senha()
user.mostrar_email()

---Atributos de instancia---
-Significa que, ao criarmos uma instancia/objetos de uma classe, todas as instancias terao estes atributos


user1 = Acesso('paula_fontenele@gmail.com','Paula123')
user2 = Acesso('math_fontenele@gmail.com', 'Matheus123')

user1.mostrar_email
user2.mostrar_email

---Atributos de classe---
-Sao atributos que terao seus proprios valores e que sempre estarao em alguma
instancia da classe

#Refatorando a classe produto
class Produto1:
    #Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto1.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto1.imposto
        Produto1.contador = self.id

p1 = Produto1('PS5','Console', 3500 )
p2 = Produto1('Xbox One', 'Console', 3200)
print(p1.id)


---Atributos Dinamicos---
-E um atributo de intancia que pode ser criado em tempo de execucao
-OBS: O atributo dinamico ser exclusivo da instancia que o criou

p3 = Produto1('frango', 'Marcearia', 5.99)
p3.peso = ('5kg')
print(f'Produto: {p3.nome}, {p3.descricao}, {p3.valor}, {p3.peso}'

#dicionario do aributo:
print(p3.__dict__)

#deletar atributo dinamicamente
del p3.peso
del p3.descricao
print(p3.__dict__)
"""
