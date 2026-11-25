"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros: desconto de 3% por litro
acima de 20 litros: desconto de 5% por litro
Gasolina:
até 20 litros: desconto de 4% por litro
acima de 20 litros: desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do
litro do álcool é R$ 1,90.
"""

litros = int(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Tipo de combustível (A/G): ").upper()

combustivel = {"A": [1.90], "G": [2.50]}

if 0 < litros <= 20:
    combustivel["A"].append(0.03)
    combustivel["G"].append(0.04)
else:
    combustivel["A"].append(0.05)
    combustivel["G"].append(0.06)

if tipo_combustivel == "G":
    preco_litro, desconto = combustivel["G"]
    valor_pago = (preco_litro * (1 - desconto)) * litros
else:
    preco_litro, desconto = combustivel["A"]
    valor_pago = (preco_litro * (1 - desconto)) * litros

print(f"Valor a ser pago: R$ {valor_pago:.2f}")
