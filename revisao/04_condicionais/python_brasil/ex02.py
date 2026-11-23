"""
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

num = int(input("Digite um valor: "))

if num > 0:
    print(f"{num} é positivo")
elif num < 0:
    print(f"{num} é negativo")
else:
    print("É zero")
