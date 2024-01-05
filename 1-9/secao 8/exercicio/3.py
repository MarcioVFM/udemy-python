"""
Faça uma função para verificar se um número é positivo ou negativo. 
Sendo que o valor de retorno sepa 1 se positivo, -1 se negativo e 0 
se for igual a 0
"""
def sinal(n):
    if n >0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
print(sinal(-12129129713))