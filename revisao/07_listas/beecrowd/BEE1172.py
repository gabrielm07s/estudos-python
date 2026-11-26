"""
beecrowd 1172 - Substituição em Vetor I
https://judge.beecrowd.com/pt/problems/view/1172
"""

VETOR = []
for i in range(10):
    VETOR.append(int(input()))

for i, X in enumerate(VETOR):
    if X <= 0:
        print(f"X[{i}] = 1")
    else:
        print(f"X[{i}] = {X}")
