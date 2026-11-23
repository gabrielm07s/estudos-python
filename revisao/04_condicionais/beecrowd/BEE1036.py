"""
beecrowd 1036 - Fórmula de Bhaskara
https://www.beecrowd.com.br/judge/pt/problems/view/1036
"""

from math import sqrt

A, B, C = map(float, input().split())
DELTA = B**2 - (4 * A * C)

if DELTA < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = (-B + sqrt(DELTA)) / (2 * A)
    R2 = (-B - sqrt(DELTA)) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
