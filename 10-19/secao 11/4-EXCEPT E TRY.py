"""
except e try

-Sao maneiras de caso de um tipo de erro no meio do seu codigo
ele faça uma outra função que voce colocar
-Pode ser de uma maneira generica, com qualquer tipo de error
que der, ou pode ser ao tratar de um error expecifico
-Geralmente e mais usado para erros especificos

#ex:
try:
    print(pao)
except:
    print('Deu um erro')

#ex2
try: 
    print(pao)
except NameError:
    print("Deu um name error")

"""
try:
    nome = 5
    print(len(nome))
except ValueError as err1:
    print(f'deu um {err1} ')
except TypeError as err2:
    print(f"Deu um {err2}")


