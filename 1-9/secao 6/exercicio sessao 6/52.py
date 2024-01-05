saque = int(input('Quanto voce deseja sacar?: '))
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
while True:
    if saque > 100:
        saque -= 100
        cem = cem + 1
    elif saque > 50:
        saque -= 50
        cinquenta = cinquenta + 1
    elif saque > 20:
        saque -= 20
        vinte = vinte + 1
    elif saque > 10:
        saque -= 10
        dez = dez + 1
    elif saque > 5:
        saque -= 5
        cinco = cinco + 1
    elif saque > 2:
        saque -= 2
        dois = dois + 1
    elif saque >= 1:
        saque -= 1
        um = um + 1
    else:
        break
print(f'{cem}:100, {cinquenta}:50, {vinte}:20, {dez}:10, {cinco}:5, {dois}:2, {um}:1 ')