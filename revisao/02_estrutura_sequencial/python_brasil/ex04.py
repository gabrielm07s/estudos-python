"""
Faça um programa que peça as 4 notas bimestrais e mostre a média.
"""

n1, n2, n3, n4 = map(float, input("Entre com as 4 notas: ").split())

media = (n1 + n2 + n3 + n4) / 4.0
print(f"A média é: {media:.2f}")
