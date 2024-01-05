"""
13- Faça uma função que receba dois vaoleres númericos e um símbolo. Este símbolo representará a operação que se deseja efetuar com os números. Se o símbolo fo +, -, / ou *
"""
def calculadora(n1, simbolo, n2):
    if simbolo == '+':
        res = n1 + n2
        return res
    elif simbolo == '-':
        res = n1 - n2
        return res
    elif simbolo == '/':
        res = n1 / n2
        return res
    elif simbolo == '*':
        res = n1 * n2
        return res
    else:
        return 'Operação invalida'
       
num1 = float(input('N1 : '))
sim = input('+, -, /, *: ')
num2 = float(input('N2: '))
print(calculadora(num1, sim, num2))