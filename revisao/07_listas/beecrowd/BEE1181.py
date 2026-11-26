"""
beecrowd 1181 - Linha na Matriz
https://judge.beecrowd.com/pt/problems/view/1181
"""

LINHA = int(input())
OPERACAO = input().upper()
MATRIZ = []

for i in range(12):
    LINHA_MATRIZ = []
    for j in range(12):
        LINHA_MATRIZ.append(float(input()))
    MATRIZ.append(LINHA_MATRIZ)

if OPERACAO == "S":
    print(f"{sum(MATRIZ[LINHA]):.1f}")

if OPERACAO == "M":
    VALOR_TOTAL_LINHA = sum(MATRIZ[LINHA])
    TOTAL_LINHA = len(MATRIZ[LINHA])
    print(f"{VALOR_TOTAL_LINHA / TOTAL_LINHA:.1f}")
