"""
*args
-Ele funciona como uma tupla, que armazena valores
infinitos nele, para nao dá nenhum erro de execução 
na função def caso seja adicionado algum valor extra
-Pode ser usado para armazenar vários valores ou só 
para pegar os valores extras daquela função

#1
def soma_dos_numeros(*args): #todos os valores que forem inseridos vao para uma tupla
    soma = 0
    soma = sum(args)
    return soma
print(soma_dos_numeros(1, 2, 3, 4, 5, 6, 7, 8))

#2
def verificador(*args):
    if 'Geek' in args and 'Universe' in args:
        return 'Ola estudante Geek'
    return 'Nao sei quem e voce'
print(verificador(1, 'Geek', 3, 5, 'Pao', 'Universe'))


-Caso queria fazer algumas operações com o *args e seja inserido 
uma lista, poderar dar Type error, tipo fazer a soma dos valores,
pois para ele fazer essa soma, será necessário desempacotala, e 
existe uma maneira facil de fazer isso

lista = [1,1,1,1,1,2,2,3,76]
def soma(*args):
    return sum(args)
#print(soma(lista))#Dará type error
print(soma(*lista))#Funcionara normal, pois a * desempacota a lista

"""
