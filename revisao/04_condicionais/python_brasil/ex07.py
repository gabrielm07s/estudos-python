"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato
"""

preco_p1 = float(input("Preço [P1]: R$ "))
preco_p2 = float(input("Preço [P2]: R$ "))
preco_p3 = float(input("Preço [P3]: R$ "))

lista_precos = [preco_p1, preco_p2, preco_p3]
indice_menor = lista_precos.index(min(lista_precos))

print(f"O menor valor é do produto {indice_menor + 1}")
