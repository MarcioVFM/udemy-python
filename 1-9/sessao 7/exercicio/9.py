lista = []
for i in range(6):
    n = int(input('escreva um numero par: '))
    par = n % 2
    while par != 0:
        n = int(input('O numero impar, digite um numeor par: '))
        par = n % 2
        if par == 0:
            lista.append(n)
    lista.append(n)
print(lista[::-1])