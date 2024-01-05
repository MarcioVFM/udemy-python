num1 = int(input('insira o primeiro numero: '))
num2 = int(input('insira o segundo numero: '))
if num1 > num2:
    print(f'O maior numero e o {num1}')
elif num1 == num2:
    print('numeros iguais')
else:
    print(f'O maior numero e o {num2}')
