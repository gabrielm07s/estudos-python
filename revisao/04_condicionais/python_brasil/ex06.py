"""
Faça um programa que leia três números e mostre o maior deles
Faça um programa que leia três números e mostre o maior e o menor deles
"""

n1, n2, n3 = map(int, input("Digite três números: ").split())
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f"O maior dos três números é: {maior}")
print(f"O menor dos três números é: {menor}")
