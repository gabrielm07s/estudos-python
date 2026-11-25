lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
for indice, valor in enumerate(lista_numeros):
    if indice % 2 == 0:
        soma += valor

print(f"Lista: {lista_numeros}")
print(f"Soma dos elementos de índices par: {soma}")
