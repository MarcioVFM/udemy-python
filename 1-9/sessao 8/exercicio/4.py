"""
Faça uma funçao que verifique se um número é umm quadrado perfeito
"""
def quadrado_perfeito(n):
    teste = int(n ** 0.5)

    if (teste ** 2) == n:
        print(f'O numero {n} é um quadrado perfeito')
        return
    print(f'O numero {n} não é um quadrado perfeito')
    return

quadrado_perfeito(8)
