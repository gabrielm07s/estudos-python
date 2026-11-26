"""
Faça um programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""

par = []
impar = []
vetor = []

for i in range(20):
    n = int(input())

    vetor.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f"Vetor: {vetor}")
print(f"Vetor par: {par}")
print(f"Vetor ímpar: {impar}")
