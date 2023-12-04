pares = []
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    par = vetor[i] % 2
    if par == 0:
        pares.append(vetor[i])
print(pares)