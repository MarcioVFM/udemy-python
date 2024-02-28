"""""
from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Fernando', 'Pedro']
versoes: Tuple[int, int, int] = (1, 2, 3)
opcoes: Dict[str, bool] = {'ar': True, 'terra': False}
valores: Set[int] = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
"""

import random
from typing import List, Tuple, Set, Dict

NAIPES = "♠ ♥ ♣ ♦ ♤ ♡ ♧ ♢".split()
CARTAS = "2 3 4 5 6 7 8 9 A J Q K".split()

CARTA = Tuple [str, str]
BARALHO = List[CARTA]

def criar_baralho(aleatorio: bool =False) -> BARALHO:
    """Cria um baralho embaralhado ou nao"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]: 
    """Gerencia a mao dos jogadores de acordo com o baralho"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar() -> None:
    """Inicia um jogo de cartas"""
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores: List[str] = "p1 p2 p3 p4".split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        cartas: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {cartas}')

if __name__ == '__main__':
    jogar()