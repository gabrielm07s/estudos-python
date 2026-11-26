"""
beecrowd 1478 - Matriz Quadrada II
https://judge.beecrowd.com/pt/problems/view/1478
"""

while True:
    N = int(input())

    if N == 0:
        break

    MATRIZ_N = [[1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        print(" ".join(f"{abs(i - j) + 1:3d}" for j in range(N)))

    print()
