"""
Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

import math

vetor = []

for i in range(5):
    n = int(input(f"Digite o {i + 1}º valor: "))

    vetor.append(n)

print(f"Vetor: {vetor}")
print(f"Soma: {sum(vetor)}")
print(f"Multiplicação {math.prod(vetor)}")
