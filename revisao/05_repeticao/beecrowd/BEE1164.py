"""
beecrowd 1164 - Número Perfeito
https://www.beecrowd.com.br/judge/pt/problems/view/1164
"""

N = int(input())

for i in range(N):
    X = int(input())

    SOMA_DIVISORES = sum([D for D in range(1, X) if X % D == 0])

    if SOMA_DIVISORES == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
