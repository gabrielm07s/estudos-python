"""
beecrowd 1165 - Número Primo
https://www.beecrowd.com.br/judge/pt/problems/view/1165
"""

N = int(input())

for i in range(N):
    X = int(input())

    DIVISORES = [D for D in range(1, X + 1) if X % D == 0]

    if len(DIVISORES) == 2:
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
