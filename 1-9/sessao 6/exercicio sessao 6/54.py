num = int(input('Escreva um numero: '))
divisor = num
while True:
    if divisor >= 1:
        divisor -= 1
        resto = num % divisor
        if resto == 0:
            print('Numero não é primo')
            break
        elif divisor == 2:
            print('Numero é primo')
            break

            