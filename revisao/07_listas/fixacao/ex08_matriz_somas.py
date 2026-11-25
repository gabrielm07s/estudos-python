matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"[{i + 1},{j + 1}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMATRIZ:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()

print(matriz)

soma_linha = [sum(x) for x in matriz]
soma_coluna = [sum(linha[j] for linha in matriz) for j in range(3)]
print(soma_linha)
print(soma_coluna)
