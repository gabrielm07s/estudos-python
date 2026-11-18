"""
beecrowd 1008 - Salário
https://www.beecrowd.com.br/judge/pt/problems/view/1008
"""

NUMBER = int(input())
HOURS_WORKED = int(input())
VALUE_PER_HOUR = float(input())

print(f"NUMBER = {NUMBER}")
print(f"SALARY = U$ {HOURS_WORKED * VALUE_PER_HOUR:.2f}")
