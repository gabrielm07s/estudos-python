# Leia 5 números e mostre quantos são pares e a soma dos ímpares
qtd_pares = 0
soma_impares = 0

for i in range(5):
    num = int(input(f'Digite o {i + 1}º número: '))

    if num % 2 == 0:
        qtd_pares += 1
    else:
        soma_impares += num

print(f'Quantidade de pares digitados: {qtd_pares}')
print(f'Soma dos ímpares digitados: {soma_impares}')