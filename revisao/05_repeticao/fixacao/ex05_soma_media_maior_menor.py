soma = 0
menor_valor = None
maior_valor = None

for i in range(1, 11):
    num = int(input("Digite um número: "))

    if maior_valor is None or num > maior_valor:
        maior_valor = num

    if menor_valor is None or num < menor_valor:
        menor_valor = num

    soma += num

print(f"Soma: {soma}")
print(f"Média: {soma / 10:.1f}")
print(f"Maior: {maior_valor}")
print(f"Menor: {menor_valor}")
