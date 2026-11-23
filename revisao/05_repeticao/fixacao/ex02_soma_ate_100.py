soma = 0
qtd_numeros = 0

contador = 1
while True:
    if soma >= 100:
        break

    num = int(input(f"Digite {contador}º número: "))

    soma += num
    qtd_numeros += 1

    print(f"[{contador}] Soma: {soma}")
    print()

    contador += 1

print(f"Soma: {soma}")
print(f"Quantidade de número: {qtd_numeros}")
