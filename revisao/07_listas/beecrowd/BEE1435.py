"""
beecrowd 1435 - Matriz Quadrada I
https://judge.beecrowd.com/pt/problems/view/1435
"""

while True:
    N = int(input())

    if N == 0:
        break

    MATRIZ_N = [[1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            cima = i
            esquerda = j
            baixo = N - 1 - i
            direita = N - 1 - j
            MATRIZ_N[i][j] = min(cima, baixo, esquerda, direita) + 1

    for linha in MATRIZ_N:
        print(" ".join(f"{valor:3d}" for valor in linha))

    print()
