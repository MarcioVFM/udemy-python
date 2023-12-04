lista = []

n = int(input('Digite um numero: '))
lista.append(n)
maior = n

for i in range(2):
    n = int(input('Digite um numero: '))
    lista.append(n)
    
    if n > maior:
        maior = n
        indice = i
print(maior, lista.index(maior))



