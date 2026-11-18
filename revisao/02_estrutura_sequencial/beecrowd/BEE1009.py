"""
beecrowd 1009 - Salário com Bônus
https://www.beecrowd.com.br/judge/pt/problems/view/1009
"""

NAME = input()
GROSS_SALARY = float(input())
TOTAL_SALES = float(input())

TOTAL = GROSS_SALARY + (TOTAL_SALES * 0.15)
print(f"TOTAL = R$ {TOTAL:.2f}")
