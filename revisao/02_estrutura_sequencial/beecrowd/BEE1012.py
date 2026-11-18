"""
beecrowd 1012 - Área
https://www.beecrowd.com.br/judge/pt/problems/view/1012
"""

PI = 3.14159
A, B, C = map(float, input().split())

TRIANGLE_AREA = (A * C) / 2.0
CIRCLE_AREA = PI * (C**2)
TRAPEZE_AREA = ((A + B) * C) / 2.0
SQUARE_AREA = B**2
RECTANGLE_AREA = A * B

print(f"TRIANGULO: {TRIANGLE_AREA:.3f}")
print(f"CIRCULO: {CIRCLE_AREA:.3f}")
print(f"TRAPEZIO: {TRAPEZE_AREA:.3f}")
print(f"QUADRADO: {SQUARE_AREA:.3f}")
print(f"RETANGULO: {RECTANGLE_AREA:.3f}")
