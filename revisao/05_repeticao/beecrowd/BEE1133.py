"""
beecrowd 1133 - Resto da Divisão
https://www.beecrowd.com.br/judge/pt/problems/view/1133
"""

X = int(input())
Y = int(input())

MAIOR, MENOR = max(X, Y), min(X, Y)

for i in range(MENOR + 1, MAIOR):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
