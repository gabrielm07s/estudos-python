"""
beecrowd 1150 - Ultrapassando
https://www.beecrowd.com.br/judge/pt/problems/view/1150
"""

X = int(input())

while True:
    Z = int(input())

    if Z > X:
        break

SOMA = 0
QTD_NUMEROS = 0

for i, numero in enumerate(range(X, Z + 1), start=1):
    if SOMA > Z:
        break

    SOMA += numero
    QTD_NUMEROS = i

print(QTD_NUMEROS)
