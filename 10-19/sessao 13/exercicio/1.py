import os
while True:
    with open ("arq.txt", "w") as arquivo:
        escrita = input('Oque voce deseja escrever?')
        arquivo.write(escrita)
    pausar = input("se desejar naos escrever mais digite '0' ")
    if pausar == '0':
        break
