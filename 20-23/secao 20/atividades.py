def dormir (num_horas):
    if num_horas > 8:
        return "Dormi muito wtfff"
    else:
        return f"to acabado, dormir so {num_horas} faz o L"


def comer (comida, e_saudavel):
    if e_saudavel:
        final = "quero viver bastante!"
    else:
        final = "so se vive uma vez :P"

    return f'Estou comendo {comida} porque {final}'
    
def eh_engracado(pessoa):
    comediantes = ['Vinicius Pereba', 'Roberta do Mal']
    if pessoa in comediantes:
        return True
    else:
        return False
    


