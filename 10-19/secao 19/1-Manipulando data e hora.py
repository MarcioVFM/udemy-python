import datetime

nascimento = input('Insira sua data de nascimento no formato dd/mm/aaaa: ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

nascimento = nascimento.date()
print(nascimento)