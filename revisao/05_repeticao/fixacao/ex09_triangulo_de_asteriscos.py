# Desenhar com asteriscos um triângulo retângulo de altura n lida
# e depois invertido
n = int(input())

print()
for linha in range(1, n + 1):
    for coluna in range(linha):
        print("*", end="")
    print()

for linha in range(n + 1, 0, -1):
    for coluna in range(1, linha):
        print("*", end="")
    print()
