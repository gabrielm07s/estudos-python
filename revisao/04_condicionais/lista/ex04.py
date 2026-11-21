# Ler valor e dizer em qual intervalo está

valor = int(input("Digite um valor: "))

if 0 <= valor < 25:
    print("[0, 25]")
elif valor < 50:
    print("[25, 50]")
elif valor < 100:
    print("[50, 100]")
else:
    print("Maior que 100...")
