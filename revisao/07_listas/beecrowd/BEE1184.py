"""
beecrowd 1184 - Abaixo da Diagonal Principal
https://judge.beecrowd.com/pt/problems/view/1184
"""

OPERACAO = input().upper()
MATRIZ = []

for i in range(12):
    LINHA = []
    for j in range(12):
        LINHA.append(float(input()))
    MATRIZ.append(LINHA)

TOTAL = sum(
    MATRIZ[LINHA][COLUNA]
    for LINHA in range(12)
    for COLUNA in range(12)
    if LINHA > COLUNA
)
QTD_TOTAL = sum(
    1 for LINHA in range(12) for COLUNA in range(12) if LINHA > COLUNA
)

if OPERACAO == "S":
    print(f"{TOTAL:.1f}")
else:
    print(f"{TOTAL / QTD_TOTAL:.1f}")
