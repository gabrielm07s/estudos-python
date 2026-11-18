"""
beecrowd 1017 - Gasto de Combustível
https://www.beecrowd.com.br/judge/pt/problems/view/1017
"""

AVERAGE_CONSUMPTION = 12

TIME_SPENT = int(input())
AVERAGE_SPEED = int(input())

DISTANCE = AVERAGE_SPEED * TIME_SPENT
LITERS_REQUIRED = DISTANCE / AVERAGE_CONSUMPTION

print(f"{LITERS_REQUIRED:.3f}")
