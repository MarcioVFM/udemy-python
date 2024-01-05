"""
Estruturas Logicas: and(e), or(ou), not(nao), is (e)

Operadores unarios:
   -not, is
operadores binarios:
   -and, or

Regras de funcionamento
and: todos os valores precisam ser True
or: apenas um dos valores precisa ser True
not: o valor do booleano e invertido, ou seja, se for True vira False
e virçe verça
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuario')
else:
    print('Voce precisa ativar sua conta')