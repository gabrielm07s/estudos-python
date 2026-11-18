"""
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
"""

n1 = int(input("Digite o primeiro número (inteiro): "))
n2 = int(input("Digite o segundo número (inteiro): "))
n3 = float(input("Digite o terceiro número (real): "))

print("\nResultados:")
print(f"O produto do dobro de {n1} com metade do {n2} é: {(2 * n1) * (n2 / 2)}")
print(f"A soma do triplo de {n1} com o {n3} é: {(3 * n1) + n3}")
print(f"O {n3} elevado ao cubo é: {n3**3}")
