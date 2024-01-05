lista = []
positivo = 0
negativo = 0
for i in range(5):
    reais = float(input('Digite o numero: '))
    lista.append(reais)
    if reais >= 0:
        positivo += reais
    else:
        negativo += reais
print(positivo, negativo)