"""
beecrowd 1182 - Coluna na Matriz
https://judge.beecrowd.com/pt/problems/view/1182
"""

COLUNA = int(input())
OPERACAO = input().upper()
MATRIZ = []

for i in range(12):
    LINHA_MATRIZ = []
    for j in range(12):
        LINHA_MATRIZ.append(float(input()))
    MATRIZ.append(LINHA_MATRIZ)

if OPERACAO == "S":
    SOMA_COLUNA = sum(C[COLUNA] for C in MATRIZ)
    print(f"{SOMA_COLUNA:.1f}")

if OPERACAO == "M":
    SOMA_COLUNA = sum(C[COLUNA] for C in MATRIZ)
    TOTAL_COLUNA = len(MATRIZ)
    print(f"{SOMA_COLUNA / TOTAL_COLUNA:.1f}")
