frase = input("Digite uma frase: ").lower()
qtd_a = 0

for letra in frase:
    if letra == "a":
        qtd_a += 1

print(f'A letra "a" apareceu {qtd_a} vezes na frase')
