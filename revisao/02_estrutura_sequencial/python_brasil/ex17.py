"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor.  Acrescente 10% de folga
e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

from math import ceil

tamanho = int(input("Tamanho da área a ser pintada: "))

LITROS_NECESSARIOS = (tamanho * 1.1) / 6

quantidade_latas = ceil(LITROS_NECESSARIOS / 18)
quantidade_galoes = ceil(LITROS_NECESSARIOS / 3.6)

latas_mistura = int(LITROS_NECESSARIOS // 18)
resto = LITROS_NECESSARIOS - latas_mistura * 18
galoes_mistura = ceil(resto / 3.6)

if galoes_mistura == 5:
    latas_mistura += 1
    galoes_mistura = 0

preco_total_latas_galoes = latas_mistura * 80 + galoes_mistura * 25

preco_total_latas = quantidade_latas * 80
preco_total_galoes = quantidade_galoes * 25


print(f"LATAS 18L: {preco_total_latas:.2f}")
print(f"GALÕES DE 3.6L: {preco_total_galoes:.2f}")
print(f"LATAS + GALÕES: {preco_total_latas_galoes:.2f}")
