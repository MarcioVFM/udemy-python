#Generator Expression
import time

gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

#List Comprehesion

list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'O tempor do GeneretorExpression:{gen_tempo}. Tempo da list: {list_tempo}')
