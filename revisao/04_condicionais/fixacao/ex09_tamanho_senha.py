senha = input("Digite a senha: ")

if (tamanho := len(senha)) >= 8:
    print(f"Maior que 8, tamanho da senha: {tamanho}")
else:
    print(f"Menor que 8, tamanho da senha: {tamanho}")
