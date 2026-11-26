"""
beecrowd 1557 - Matriz Quadrada III
https://judge.beecrowd.com/pt/problems/view/1557
"""

while True:
    N = int(input())

    if N == 0:
        break

    MATRIZ_N = [[2 ** (i + j) for j in range(N)] for i in range(N)]
    LARGURA = len(str(MATRIZ_N[-1][-1]))

    for linha in MATRIZ_N:
        print(" ".join(f"{valor:{LARGURA}d}" for valor in linha))

    print()
