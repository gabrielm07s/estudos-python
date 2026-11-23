# Mostrar cada letra de uma palavra com a posição usando enumerate
palavra = input("Digite uma palavra: ")

for indice, letra in enumerate(palavra):
    print(indice, letra)
