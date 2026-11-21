# Ler dois números e dizer se são múltiplos um do outro
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 % n2 == 0:
    print(f"{n1} é múltiplo de {n2}")
elif n2 % n1 == 0:
    print(f"{n1} é divisor de {n2}")
else:
    print("Não são múltiplos")
