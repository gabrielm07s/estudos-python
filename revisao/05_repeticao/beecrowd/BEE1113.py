"""
beecrowd 1113 - Crescente e Decrescente
https://www.beecrowd.com.br/judge/pt/problems/view/1113
"""

while True:
    X, Y = map(int, input().split())

    if X == Y:
        break

    print(f"{'Crescente' if X < Y else 'Decrescente'}")
