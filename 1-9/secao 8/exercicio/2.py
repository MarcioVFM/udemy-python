"""
Faça uma função que receba a datra atual (dia, mês e ano em inteiro)
e exiba-a na tela no formato textual por extenso
"""
def data(dia, mes, ano):
    if mes == 1:
        mes = 'Janeiro'
    elif mes == 2:
        mes = 'Fevereiro'
    elif mes == 3:
        mes = 'Março'
    elif mes == 4:
        mes = 'Abril'
    elif mes == 5:
        mes = 'Maio'
    elif mes == 6:
        mes = 'Junho'
    elif mes == 7:
        mes = 'Julho'
    elif mes == 8:
        mes = 'Agosto'
    elif mes == 9:
        mes = 'Setembro'
    elif mes == 10:
        mes = 'Outubro'
    elif mes == 11:
        mes = 'Novembro'
    elif mes == 12:
        mes = 'Dezembro'
    else:
        print("numero do mes inserido invalido")
        return
    print(f'{dia} de {mes} de {ano}')
data(10, 3, 2000)





