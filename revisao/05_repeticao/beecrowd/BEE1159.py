"""
beecrowd 1159 - Soma de Pares Consecutivos
https://www.beecrowd.com.br/judge/pt/problems/view/1159
"""

while True:
    X = int(input())

    if X == 0:
        break

    SOMA_PARES = 0

    for i in range(5):
        if X % 2 != 0:
            X += 1

        if X % 2 == 0:
            SOMA_PARES += X
            X += 2

    print(SOMA_PARES)
