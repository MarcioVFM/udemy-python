salario = float(input('Digite o seu salario: '))
emprestimo = float(input('Digite o quanto voce quer de emprestimo: '))
minimo = salario * 0.2
if emprestimo > minimo:
    print('emprestimo não concedido')
else:
    print('emprestimo concedido')