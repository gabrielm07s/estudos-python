"""
beecrowd 1071 - Soma de Ímpares Consecutivos I
https://www.beecrowd.com.br/judge/pt/problems/view/1071
"""

X = int(input())
Y = int(input())
MAIOR, MENOR = max(X, Y), min(X, Y)
SOMA_IMPARES = 0

for i in range(MENOR + 1, MAIOR):
    if i % 2 != 0:
        SOMA_IMPARES += i

print(SOMA_IMPARES)
