"""
beecrowd 1173 - Preenchimento de Vetor I
https://judge.beecrowd.com/pt/problems/view/1173
"""

VETOR = []
N = int(input())

for i in range(10):
    VETOR.append(N)
    N *= 2

for i, _ in enumerate(VETOR):
    print(f"N[{i}] = {VETOR[i]}")
