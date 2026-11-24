"""
beecrowd 1158 - Soma de Ímpares Consecutivos III
https://www.beecrowd.com.br/judge/pt/problems/view/1158
"""

N = int(input())

for i in range(N):
    X, Y = map(int, input().split())

    SOMA_IMPARES = 0

    for j in range(1, Y + 1):
        if X % 2 == 0:
            X += 1

        if X % 2 != 0:
            SOMA_IMPARES += X
            X += 2

    print(SOMA_IMPARES)
