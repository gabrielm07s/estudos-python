"""
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lado = float(input("Lado do quadrado: "))

area = lado**2

print(f"Área do quadrado: {area:.2f}")
print(f"Dobro da área: {area * 2}")
