"""
-Generetors sao usados pois tem um baixo uso de 
memoria
-Nao quer dizer que serao mais rapidos
-Ex de uso: sequencia de fibonacci
oque e: 1, 1, 3, 3, 5, 8, 13....
sempre somando com o seu antecessor
"""
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

for n in fib_lista(100000):
    print(n)