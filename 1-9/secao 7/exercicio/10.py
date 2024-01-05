nota = []
total = 0
for i in range(3):
    n = float(input('Digite a nota do aluno: '))
    nota.append(n)
    total += n
media = total / 3
print(media)
