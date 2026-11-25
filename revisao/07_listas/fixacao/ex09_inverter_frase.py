frase = input()
palavras = frase.split()

palavras_invertidas = palavras[::-1]
frase_invertida = " ".join(palavras_invertidas)

print()
print(f"Original: {frase}")
print(f"Invertida: {frase_invertida}")
