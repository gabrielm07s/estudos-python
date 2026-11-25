"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base, expoente = map(int, input("Base e Expoente: ").split())
resultado = 1
for i in range(expoente):
    resultado *= base

print(resultado)
