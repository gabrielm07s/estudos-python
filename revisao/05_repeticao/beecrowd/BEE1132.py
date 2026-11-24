"""
beecrowd 1132 - Múltiplos de 13
https://www.beecrowd.com.br/judge/pt/problems/view/1132
"""

X = int(input())
Y = int(input())

MAIOR, MENOR = max(X, Y), min(X, Y)
SOMA = 0

for i in range(MENOR, MAIOR + 1):
    if i % 13 != 0:
        SOMA += i

print(SOMA)
