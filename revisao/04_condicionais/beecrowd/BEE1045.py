"""
beecrowd 1045 - Tipos de Triângulos
https://www.beecrowd.com.br/judge/pt/problems/view/1045
"""

A, B, C = sorted(map(float, input().split()), reverse=True)

NAO_EXISTE_TRIANGULO = A >= B + C

if not NAO_EXISTE_TRIANGULO:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B == C):
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")
