"""
beecrowd 1042 - Simple Sort
https://www.beecrowd.com.br/judge/pt/problems/view/1042
"""

A, B, C = map(int, input().split())

NUMEROS_ORDENADO = [A, B, C]
NUMEROS_ORDENADO.sort()

for N in NUMEROS_ORDENADO:
    print(N)

print()

for N in (A, B, C):
    print(N)
