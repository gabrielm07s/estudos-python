numero = 1234
original = numero
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print(f"Original: {original}")
print(f"Invertido: {invertido}")
