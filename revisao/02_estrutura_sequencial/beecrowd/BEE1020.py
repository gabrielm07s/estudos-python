"""
beecrowd 1020 - Idade em Dias
https://www.beecrowd.com.br/judge/pt/problems/view/1020
"""

AGE = int(input())

YEARS = AGE // 365
REST = AGE % 365
MONTHS = REST // 30
REST %= 30
DAYS = REST

print(f"{YEARS} ano(s)")
print(f"{MONTHS} mes(es)")
print(f"{DAYS} dia(s)")
