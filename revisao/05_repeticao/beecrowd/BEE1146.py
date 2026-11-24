"""
beecrowd 1146 - Sequência Crescente
https://www.beecrowd.com.br/judge/pt/problems/view/1146
"""

while True:
    X = int(input())

    if X == 0:
        break

    print(" ".join(str(i) for i in range(1, X + 1)))
