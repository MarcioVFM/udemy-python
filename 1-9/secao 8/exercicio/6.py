def segundos(h=0, m=0, s=0):
    totals = h * 3600
    totals += m * 60
    totals += 60
    return totals
print(segundos(20, m=10, s=30)) 