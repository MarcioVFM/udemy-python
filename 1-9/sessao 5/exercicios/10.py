h = float(input('Digite sua altura: '))
sexo = (input('Digite o seu sexo ("Homem ou Mulher"): '))
if sexo == 'Homem':
    peso = (72.7 * h) - 58
    print(f'Seu peso ideal e {peso}')
else:
    peso = (62.1 * h) - 44.7
    print(f'Seu peso ideal e {peso}')