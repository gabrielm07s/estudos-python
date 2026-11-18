"""
beecrowd 1015 - Distância Entre Dois Pontos
https://www.beecrowd.com.br/judge/pt/problems/view/1015
"""

from math import sqrt

(X1, Y1) = map(float, input().split())
(X2, Y2) = map(float, input().split())

DISTANCE_AB = sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))
print(f"{DISTANCE_AB:.4f}")
