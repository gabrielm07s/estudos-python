"""
beecrowd 1149 - Somando Inteiros Consecutivos
https://www.beecrowd.com.br/judge/pt/problems/view/1149
"""

VALORES = list(map(int, input().split()))
A, N = [x for x in VALORES if x > 0]
SOMA = 0

for i in range(N):
    SOMA += A + i

print(SOMA)
