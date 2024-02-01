"""
Assertions (Checagens ou Questionamentos)

em pytohn, utilizamos a palavra reservada 'assert' para realizar simples
afirmacoes utitilizadas nos testes

utilizamos o 'assert' em uma expressao que queremos checar se e validar ou nao
Se a expressao for verdadeira, retorna None e caso seja falsa levanta um error

#OBS: Nos podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de error personalizada
- A palavra 'assert' pode ser utulizada em qualquer funcao ou codigo nosso, nnao presia
ser exclusivamente os testes

---nao e muito bom usar o assert, pois se voce rodar o codigo com 
um -O, ele sera desligado

"""

def soma_positivo(a, b):
    assert a > 0 and b > 0, "os numeros tem que ser posivitos"
    return a + b

soma1 = soma_positivo(1, 2)
print(soma1)
#soma1 = soma_positivo(-2, 2)
#print(soma1)