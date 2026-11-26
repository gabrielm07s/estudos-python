"""
beecrowd 1178 - Preenchimento de Vetor III
https://judge.beecrowd.com/pt/problems/view/1178
"""

X = float(input())
N = []

for i in range(100):
    N.append(X)
    X /= 2

for i, _ in enumerate(N):
    print(f"N[{i}] = {N[i]:.4f}")
