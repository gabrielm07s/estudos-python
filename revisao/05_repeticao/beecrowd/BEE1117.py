"""
beecrowd 1117 - Validação de Nota
https://www.beecrowd.com.br/judge/pt/problems/view/1117
"""

SOMA_NOTAS = 0
QTD_NOTAS = 0

while True:
    N = float(input())

    if not 0 <= N <= 10:
        print("nota invalida")
        continue

    SOMA_NOTAS += N
    QTD_NOTAS += 1

    if QTD_NOTAS == 2:
        break


MEDIA = SOMA_NOTAS / 2.0
print(f"media = {MEDIA:.2f}")
