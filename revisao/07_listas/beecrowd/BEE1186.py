"""
beecrowd 1186 - Abaixo da Diagonal Secundária
https://judge.beecrowd.com/pt/problems/view/1186
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
    if LINHA + COLUNA > len(MATRIZ) - 1
)
QTD_TOTAL = sum(
    1
    for LINHA in range(12)
    for COLUNA in range(12)
    if LINHA + COLUNA > len(MATRIZ) - 1
)

if OPERACAO == "S":
    print(f"{TOTAL:.1f}")
else:
    print(f"{TOTAL / QTD_TOTAL:.1f}")
