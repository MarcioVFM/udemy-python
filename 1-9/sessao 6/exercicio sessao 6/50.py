anos = 0
chico = 1.50
ze = 1.10
while True:
    anos = anos + 1
    chico = chico + 0.2
    ze = ze + 0.3
    if ze > chico:
        break
print(f"Ze demorou {anos} anos para passar Chico na altura")