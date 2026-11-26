"""
Faça um programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

for i in range(4):
    n = float(input(f"Digite a {i + 1}º nota: "))
    notas.append(n)

media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")
