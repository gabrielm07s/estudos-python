"""
João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

PESO_REGULAMENTADO = 50  # kg
peso = float(input("Digite o peso (kg): "))
peso_excedente = 0

if peso > PESO_REGULAMENTADO:
    peso_excedente = peso - PESO_REGULAMENTADO

MULTA = 4 * peso_excedente

print(f"Peso excedente: {peso_excedente}")
print(f"Multa a ser paga: R$ {MULTA:.2f}")
