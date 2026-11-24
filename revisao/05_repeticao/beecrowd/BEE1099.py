"""
beecrowd 1099 - Soma de Ímpares Consecutivos II
https://www.beecrowd.com.br/judge/pt/problems/view/1099
"""

N = int(input())

for i in range(N):
    X, Y = map(int, input().split())
    MAIOR, MENOR = max(X, Y), min(X, Y)

    SOMA_IMPARES = 0
    for j in range(MENOR + 1, MAIOR):
        if j % 2 != 0:
            SOMA_IMPARES += j
    print(SOMA_IMPARES)
