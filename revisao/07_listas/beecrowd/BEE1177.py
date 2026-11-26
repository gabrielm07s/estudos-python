"""
beecrowd 1177 - Preenchimento de Vetor II
https://judge.beecrowd.com/pt/problems/view/1177
"""

T = int(input())
VETOR = []

i = 0
for _ in range(1000):
    if i == T:
        i = 0
    VETOR.append(i)
    i += 1

for i, N in enumerate(VETOR):
    print(f"N[{i}] = {N}")
