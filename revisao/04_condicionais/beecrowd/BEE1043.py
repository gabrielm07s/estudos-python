"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

Exemplo de Entrada	Exemplo de Saída
6.0 4.0 2.0
Area = 10.0

6.0 4.0 2.1
Perimetro = 12.1
"""

A, B, C = map(float, input().split())
EXISTE_TRIANGULO = (A < B + C) and (B < A + C) and (C < A + B)

if EXISTE_TRIANGULO:
    PERIMETRO = sum((A, B, C))
    print(f"Perimetro = {PERIMETRO:.1f}")
else:
    AREA = ((A + B) * C) / 2.0
    print(f"Area = {AREA:.1f}")
