lista = []

n = int(input('Digite um numero: '))
lista.append(n)
maior = n
menor = n

for i in range(2):
    n = int(input('Digite um numero: '))
    lista.append(n)
    
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(maior, lista.index(maior))
print(menor, lista.index(menor))