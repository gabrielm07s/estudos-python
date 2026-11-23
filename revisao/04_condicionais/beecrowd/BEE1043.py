"""
beecrowd 1043 - Triângulo
https://www.beecrowd.com.br/judge/pt/problems/view/1043
"""

A, B, C = map(float, input().split())
EXISTE_TRIANGULO = (A < B + C) and (B < A + C) and (C < A + B)

if EXISTE_TRIANGULO:
    PERIMETRO = sum((A, B, C))
    print(f"Perimetro = {PERIMETRO:.1f}")
else:
    AREA = ((A + B) * C) / 2.0
    print(f"Area = {AREA:.1f}")
