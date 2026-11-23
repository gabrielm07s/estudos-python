# Contando vogais
frase = input("Digite a frase: ").lower()
vogais = ["a", "e", "i", "o", "u"]

qtd_vogais = 0

for letra in frase:
    if letra in vogais:
        qtd_vogais += 1

print(f"Quantidade de vogais presentes na frase: {qtd_vogais}")
