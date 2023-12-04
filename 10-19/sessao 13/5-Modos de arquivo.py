"""
Modos de arquivo

r-> Abre o arquivo pra leitura
w-> Abre o arquivo para escrever, porem apaga tudo que tiver nele,
e se nao existir cria um 
x->Abre um arquivo para escrita somente se nao existir um
a-> Abre um arquivo para escrita, e escreve no FINAL dele
+-> Ele funciona como um adicional, deixa controlar o cursor


"""
with open ('teste/texto.txt', 'r+') as arquivo:
    arquivo.write('adicionando\n')
    arquivo.seek(34)
    arquivo.write(' teste kk')