frase = input().strip().lower().replace(" ", "")
letras = {}

for letra in frase:
    letras[letra] = letras.get(letra, 0) + 1

print(letras)
