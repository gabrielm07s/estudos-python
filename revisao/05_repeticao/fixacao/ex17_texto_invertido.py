# Mostrar letras de um texto de trás para frente de três jeitos:
# range, reversed, fatiamento
texto = input("Texto: ")

print()
print(f"Texto original: {texto}")

texto_invertido = list(reversed(texto))
print("Texto invertido com reversed:", end=" ")
for letra in texto_invertido:
    print(letra, end="")

print()
print("Texto invertido com range:", end=" ")
for letra in range(len(texto) - 1, -1, -1):
    print(texto[letra], end="")

print(f"\nTexto invertido: {texto[::-1]}")
