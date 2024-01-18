"""
Delta

-É a diferenca entre duas datas, ums inicial e uma final


import datetime

aniversario = datetime.datetime(2024, 3, 30)
data_hoje = datetime.datetime.now()
tempo_aniversario = aniversario - data_hoje
print(tempo_aniversario.days)
"""
import datetime

boleto_gerado = datetime.datetime.now()
print(boleto_gerado)

regra_boleto = datetime.timedelta(days = 3)
print(regra_boleto)

vencimeto = boleto_gerado + regra_boleto
print(vencimeto)

