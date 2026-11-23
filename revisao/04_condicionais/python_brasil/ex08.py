"""
Faça um programa que leia três números e mostre-os em ordem decrescente:
"""

lista_numeros = list(map(int, input().split()))
lista_numeros.sort(reverse=True)
print(*lista_numeros)
