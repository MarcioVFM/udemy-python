n = int(input(f'Digite o número de linhas: '))

m = 1
for c in range(1, n + 1):
    for i in range(1, c + 1):
        print(f'{m:<4}', end='')
        m += 1
    print()