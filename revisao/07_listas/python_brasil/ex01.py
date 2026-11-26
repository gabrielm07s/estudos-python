"""
Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
"""

vetor = []

for i in range(5):
    n = int(input(f"Digite o {i + 1}º valor: "))
    vetor.append(n)

print(vetor)
