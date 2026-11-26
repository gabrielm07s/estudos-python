"""
beecrowd 1174 - Seleção em Vetor I
https://judge.beecrowd.com/pt/problems/view/1174
"""

VETOR = []

for i in range(100):
    VETOR.append(float(input()))

for i, A in enumerate(VETOR):
    if A <= 10:
        print(f"A[{i}] = {A:.1f}")
