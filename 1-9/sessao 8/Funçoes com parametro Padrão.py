"""
Parametro padrao

-É um parametro que nao e obrigatorio ter um valor para ele funcionar, se nao colocar um valor nao dara 
nenhum error tambem
-Ele tera um valor pre-definido se nao for colocado nada

total = 0
def contador(n=0, c=10):
    for i in range(c + 1):
       n = 1 + n
    return n, c
total, numero = contador(total, 9)
print(total, numero)


-O parametro padrao ele sempre tem que se o ultimo na declaração do def, senao dara error

-Ex1 de parametro padrao
def expodencial(num, ex=2):
    num = num ** ex
    return num

print(expodencial(2,3))

-Ex2
def mostrar_informação (nome='Geek', intrutor=False):
    if nome == 'Geek' and intrutor == True:
        return 'Bem vindo estrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que voce era um instrutor Geek'
    return f'Ola {nome}'
print(mostrar_informação())
print(mostrar_informação(intrutor=True))
print(mostrar_informação('Pedro'))


-Existem tambem variaveis que sao globais e locais, as variaveis locais
-A variavel local tem preferencia sobre a variavel global

professor = 'Joao' #variavel global
def nome():
   professor = 'Raimundo' #variavel local
   return professor #Raimundo

-Como usar as variaveis globais 
numero = 0
def contador():
   numero = numero + 1 #dara error
   return numero

def contador():
   global numero #ele ira utilizar a variavel global
   numero = numero + 1 #dara error
   return numero

-Usar uma variavel e uma função anterior 
def fora():
   contador = 0
   def dentro():
      nonlocal contador
      contador += 1
      return contador
    return dentro()
"""

