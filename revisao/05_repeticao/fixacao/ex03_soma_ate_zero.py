soma = 0
qtd_num = 0

while qtd_num < 10:
    num = int(input(f"Digite o {qtd_num + 1}º número: "))

    if num < 0:
        continue

    if num == 0:
        break

    soma += num
    qtd_num += 1

print(f"\nSoma dos números: {soma}")
