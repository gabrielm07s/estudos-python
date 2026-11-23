"""
Faça um programa que peça dois números e imprima o maior deles.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"{n1} é o maior")
elif n2 > n1:
    print(f"{n2} é maior")
else:
    print("Os dois são iguais")
