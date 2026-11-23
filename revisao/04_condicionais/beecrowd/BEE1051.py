"""
beecrowd 1051 - Imposto de Renda
https://www.beecrowd.com.br/judge/pt/problems/view/1051
"""

SALARIO = float(input())
IR = 0

if 0 < SALARIO <= 2000:
    print("Isento")
else:
    IR = 0.0

    if SALARIO > 4500.0:
        IR += (SALARIO - 4500.0) * 0.28
        SALARIO = 4500.0

    if SALARIO > 3000.0:
        IR += (SALARIO - 3000.0) * 0.18
        SALARIO = 3000.0

    if SALARIO > 2000.0:
        IR += (SALARIO - 2000.0) * 0.08

    print(f"R$ {IR:.2f}")
