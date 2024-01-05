num1 = int(input('insira o primeiro numero: '))
num2 = int(input('insira o segundo numero: '))
if num1 > num2:
    dif = num1 - num2
    print(f'O maior numero e o {num1} e a sua diferença é {dif}')
else:
    dif = num2 - num1
    print(f'O maior numero e o {num2} e a sua diferença é {dif}')