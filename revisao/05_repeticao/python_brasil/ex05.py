"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

num = int(input("Digite um número: "))
numeros_primos = []

for i in range(2, num + 1):
    divisores = [x for x in range(1, i + 1) if i % x == 0]
    if len(divisores) == 2:
        numeros_primos.append(i)

print(f"Números primos até {num}: {numeros_primos}")
