"""
Saido de loops bom Breaks

Utilizamos o break para sair do loop de forma projetada

#exemplo 1
for numero in range (1,11):
    if numero == 6:
        break
    else:
        print (numero)
print(' loop foi parado')

"""
#Exemplo 2
numero = int(input('digite um numero para mostrar seu quadrado ate 1000: '))
while True:
    numero = numero ** 2
    print(numero)
    if numero > 1000:
        break