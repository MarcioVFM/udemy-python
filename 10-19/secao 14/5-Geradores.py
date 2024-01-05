"""
funcoes x geradores
-funcoes:                                  geradores:
utilizam return                            utilizam yield
retorna uma vez                            podem utilizar yield multiplas vezes
quando executada, retorna um valor         quando executada, retorna um generator



"""
def contador(valor_max):
    contador = 1
    while valor_max > contador:
        yield contador
        contador = contador + 1

valorr = contador(5)
for valor in valorr:
    print(valor)
