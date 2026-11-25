"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível.
"""

num = int(input("Digite um número: "))
divisores = [x for x in range(1, num + 1) if num % x == 0]

if len(divisores) == 2:
    print(f"{num} é primo: {divisores}")
else:
    print(f"{num} é composto: {divisores}")
