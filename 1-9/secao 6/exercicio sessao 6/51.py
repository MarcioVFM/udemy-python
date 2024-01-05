Ano = int(input('em que ano estamos?: '))
ano = Ano - 1995
aumento = 0.015
salario = 2000
for i in range (0, ano):
    salario = salario + salario * aumento
    aumento = aumento * 2
print(f'Seu salario atual é {salario}')