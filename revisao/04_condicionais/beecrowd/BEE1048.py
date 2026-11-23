"""
beecrowd 1048 - Cálculo de Reajuste
https://www.beecrowd.com.br/judge/pt/problems/view/1048
"""

SALARIO = float(input())
PERCENTUAL = 0

if 0 < SALARIO <= 400.00:
    PERCENTUAL = 15
elif SALARIO <= 800:
    PERCENTUAL = 12
elif SALARIO <= 1200:
    PERCENTUAL = 10
elif SALARIO <= 2000:
    PERCENTUAL = 7
else:
    PERCENTUAL = 4

NOVO_SALARIO = SALARIO * (1 + (PERCENTUAL / 100))
REAJUSTE = SALARIO * (PERCENTUAL / 100)

print(f"Novo salario: {NOVO_SALARIO:.2f}")
print(f"Reajuste ganho: {REAJUSTE:.2f}")
print(f"Em percentual: {PERCENTUAL} %")
