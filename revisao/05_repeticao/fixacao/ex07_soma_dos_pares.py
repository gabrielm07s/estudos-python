# Mostre a soma dos números pares de 1 a 100 de duas formas:
# com if e com o passo do range
soma_pares = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma_pares += i

# for i in range(0, 101, 2):
#     soma_pares += i

print(f"Soma dos pares: {soma_pares}")
