# Percorrer dois textos com zip e contar as posições
# em que as letras são diferentes
texto1 = input("Digite o primeiro texto: ")
texto2 = input("Digite o segundo texto: ")

posicoes_diferente = 0
for indice, letras in enumerate(zip(texto1, texto2)):
    if letras[0] != letras[1]:
        posicoes_diferente += 1

print(f"Posições diferentes: {posicoes_diferente}")
