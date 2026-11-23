"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
15% 0 - 400.00
12% 400.01 - 800.00
10% 800.01 - 1200.00
7% 1200.01 - 2000.00
4% Acima de 2000.00

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado,
em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
400.00
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

800.01
Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

2000.00
Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
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
