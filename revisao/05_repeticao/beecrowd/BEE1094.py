"""
beecrowd 1094 - Experiências
https://www.beecrowd.com.br/judge/pt/problems/view/1094
"""

N = int(input())
COBAIAS = {"R": 0, "S": 0, "C": 0}

for i in range(N):
    QUANTIA, TIPO = input().split()
    COBAIAS[TIPO] += int(QUANTIA)

TOTAL_COBAIAS = sum(COBAIAS.values())
PERCENTUAL_COBAIA_C = (COBAIAS["C"] / TOTAL_COBAIAS) * 100
PERCENTUAL_COBAIA_R = (COBAIAS["R"] / TOTAL_COBAIAS) * 100
PERCENTUAL_COBAIA_S = (COBAIAS["S"] / TOTAL_COBAIAS) * 100

print(f"Total: {TOTAL_COBAIAS} cobaias")
print(f"Total de coelhos: {COBAIAS['C']}")
print(f"Total de ratos: {COBAIAS['R']}")
print(f"Total de sapos: {COBAIAS['S']}")
print(f"Percentual de coelhos: {PERCENTUAL_COBAIA_C:.2f} %")
print(f"Percentual de ratos: {PERCENTUAL_COBAIA_R:.2f} %")
print(f"Percentual de sapos: {PERCENTUAL_COBAIA_S:.2f} %")
