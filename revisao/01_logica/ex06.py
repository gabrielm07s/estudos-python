# Contar vogais em frase
frase = input('Digite uma frase: ').lower()

vogais = ['a', 'e', 'i', 'o', 'u']
qtd_vogais = 0

for letra in frase:
    if letra in vogais:
        qtd_vogais += 1

print(f'Na frase: "{frase}" existem {qtd_vogais} vogais')