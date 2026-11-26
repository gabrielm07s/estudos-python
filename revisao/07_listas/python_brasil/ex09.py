"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor_a = []

for i in range(10):
    vetor_a.append(int(input(f"Digite o {i + 1}º valor: ")))

print(f"Vetor: {vetor_a}")
print(f"Soma dos quadrados: {sum([x**2 for x in vetor_a])}")
