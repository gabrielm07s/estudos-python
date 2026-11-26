"""
beecrowd 1175 - Troca em Vetor I
https://judge.beecrowd.com/pt/problems/view/1175
"""

VETOR = []

for i in range(20):
    VETOR.append(int(input()))

VETOR_INVERTIDO = VETOR[::-1]

for i, N in enumerate(VETOR_INVERTIDO):
    print(f"N[{i}] = {N}")
