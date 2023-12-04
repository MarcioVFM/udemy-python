"""
Manipulação de arquivos

#1 Passo: descobrir se o diretorio existe
import os

print(os.path.exists('estudo'))
print(os.path.exists('estudo\\faculdade'))

#2 Passo: criar um arquivo

with open("criando.aquirvo","w") as arquivo:
    arquivo.write("criei o arquivo")
    arquivo.write("\ndiretorio dessa criacao: estudo\\udemy python\\10-19\\sessao13")

#3 criando diretorios
import os
os.mkdir("zdiretorio.criado")

#4 multiplos diretorios
import os
os.makedirs("znao abra\\nao abra pf\\fodase?")

#5 renomeando diretorios e arquivos
import os
os.rename("znao abra", "zabra")
"""
#6 arquivos temporarios
import os
import tempfile
with tempfile.TemporaryDirectory() as temp:
    print("foi criado um arquivo temporario")
    with open(os.path.join(temp, 'arquivo_temporario'), "w") as arquivo:
        arquivo.write("teste de temporario")
    input()
#Estamos criando um diretorio temporario, abrindo o mesmo e dentro dele
#criando um arqiov ára escrevermos um texto. No final, usamos um input()
#so para mantermos os arquivos temporarios 'vivos' dentro dos blocos with

#Nao funciuona no windows
