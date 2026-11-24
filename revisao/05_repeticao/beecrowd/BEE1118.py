"""
beecrowd 1118 - Várias Notas Incorretas
https://www.beecrowd.com.br/judge/pt/problems/view/1118
"""

import sys

SOMA_NOTAS = 0.0
QTD_NOTAS = 0

while True:
    N = float(input())

    if not 0 <= N <= 10:
        print("nota invalida")
        continue

    SOMA_NOTAS += N
    QTD_NOTAS += 1

    if QTD_NOTAS == 2:
        MEDIA = SOMA_NOTAS / 2.0
        print(f"media = {MEDIA:.2f}")

        while True:
            print("novo calculo (1-sim 2-nao)")
            X = int(input())

            if X == 1:
                SOMA_NOTAS = 0.0
                QTD_NOTAS = 0
                break
            elif X == 2:
                sys.exit()
