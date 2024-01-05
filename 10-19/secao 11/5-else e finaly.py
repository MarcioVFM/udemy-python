"""
else e finaly

-O else ele so ira funcionar se o try nao der nenhum erro,
assim evitando outros possiveis erros caso o que tenha sido 
escrito no try nao seja rodado
-O finaly ele ira rodar no final de tudo independente do que
aconteça, tendo sua utilidade em fechar ou desalocar recursos

#ex1:
try:
    num = int(input("Escreva um numero: "))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Numero digitado: {num}')
finally:
    print('Final')


#ex2 complexo errado
def dividir(a, b):
    try:
       return a / b
    except ZeroDivisionError:
        print('Nao pode dividir um numero por zero')
try:
    num1 = int(input("digite um numero: "))
    num2 = int(input("Digite outro numero: "))
except ValueError:
    print('Numero digitado incorreto')
else:
    print(dividir(num1, num2))
finally:
    print('fim')
"""

#ex3 complexo certo:
def divisao(a, b):
    try:
        return int(a) / int(b)
    except ValueError: #Especificar o erro para aparecer a mensagem de acordo com o tipo de erro para o usuario
        return'Valor digitado nao confere'
    except ZeroDivisionError:
        return'Nao e divisivel por 0'
num1 = (input('Digite o primeiro numero: '))
num2 = (input('Digite o segundo: ')) 
print(divisao(num1, num2))   