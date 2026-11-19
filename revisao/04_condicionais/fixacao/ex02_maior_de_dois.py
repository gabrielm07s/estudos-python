n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 == n2:
    print("Os dois números são iguais")
else:
    maior = max(n1, n2)
    print(f"O maior entre {n1} e {n2} é {maior}")
