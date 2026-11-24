"""
beecrowd 1115 - Quadrante
https://www.beecrowd.com.br/judge/pt/problems/view/1115
"""

while True:
    X, Y = map(int, input().split())

    if X == 0 or Y == 0:
        break

    if X > 0 and Y > 0:
        print("primeiro")
    elif X > 0 and Y < 0:
        print("quarto")
    elif X < 0 and Y < 0:
        print("terceiro")
    elif X < 0 and Y > 0:
        print("segundo")
