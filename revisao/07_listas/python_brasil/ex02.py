"""
Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

vetor = []

for i in range(10):
    n = float(input(f"Digite o {i + 1}º número: "))
    vetor.append(n)

print(f"Original: {vetor}")
print(f"Inverso: {vetor[::-1]}")
