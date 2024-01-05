from random import random
def jogar_moeda():
   if random() > 0.5:
      return 'cara'
   return 'coroa'
print(jogar_moeda())