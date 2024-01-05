vetor = []

n = int(input('Digite um numero: '))
vetor.append(n)
maior = n
menor = n
for i in range(9):
    n = int(input('Digite um numero: '))
    vetor.append(n)

    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior numero: {maior}')
print(f'O menor numero: {menor}')

"""
jeito facil de fazer

vetor = []
for i in range(10):
    n = int(input('Digite um numero: '))
    vetor.append(n)
print(max(vetor))
print(min(vetor))
"""
