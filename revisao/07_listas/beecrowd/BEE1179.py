"""
beecrowd 1179 - Preenchimento de Vetor IV
https://judge.beecrowd.com/pt/problems/view/1179
"""

PARES = []
IMPARES = []

for i in range(15):
    X = int(input())

    if len(PARES) == 5:
        for i, N in enumerate(PARES):
            print(f"par[{i}] = {N}")
        PARES = []

    if len(IMPARES) == 5:
        for i, N in enumerate(IMPARES):
            print(f"impar[{i}] = {N}")
        IMPARES = []

    if X % 2 == 0:
        PARES.append(X)
    else:
        IMPARES.append(X)

if len(IMPARES) > 0:
    for i, N in enumerate(IMPARES):
        print(f"impar[{i}] = {N}")

if len(PARES) > 0:
    for i, N in enumerate(PARES):
        print(f"par[{i}] = {N}")
