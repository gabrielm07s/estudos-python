"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

from math import ceil

tamanho = float(input("Digite o tamanho em m² da área a ser pintada: "))

LITROS_NECESSARIOS = tamanho / 3
quantidade_latas = ceil(LITROS_NECESSARIOS / 18)
preco_total = quantidade_latas * 80

print(f"Quantidade de latas de tinta necessárias: {quantidade_latas}")
print(f"Preço total: {preco_total:.2f}")
