"""
beecrowd 1183 - Acima da Diagonal Principal
https://judge.beecrowd.com/pt/problems/view/1183
"""

OPERACAO = input().upper()
MATRIZ = []

for i in range(12):
    LINHA_MATRIZ = []
    for j in range(12):
        LINHA_MATRIZ.append(float(input()))
    MATRIZ.append(LINHA_MATRIZ)

TOTAL = sum(
    MATRIZ[LINHA][COLUNA]
    for LINHA in range(12)
    for COLUNA in range(12)
    if COLUNA > LINHA
)
QTD_TOTAL = sum(
    1 for LINHA in range(12) for COLUNA in range(12) if COLUNA > LINHA
)

if OPERACAO == "S":
    print(f"{TOTAL:.1f}")
else:
    print(f"{TOTAL / QTD_TOTAL:.1f}")
