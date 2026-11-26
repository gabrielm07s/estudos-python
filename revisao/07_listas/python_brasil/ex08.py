"""
Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

l_idade = []
l_altura = []

for i in range(5):
    print(f"Pessoa {i + 1}º: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))

    l_idade.append(idade)
    l_altura.append(altura)
    print()

print(f"Original: {list(zip(l_idade, l_altura))}")
print(f"Inversa: {list(zip(l_idade, l_altura))[::-1]}")
