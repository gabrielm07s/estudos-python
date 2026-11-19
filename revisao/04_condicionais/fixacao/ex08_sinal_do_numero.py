n = int(input("Digite um número: "))

match n:
    case n if n < 0:
        print("Negativo")
    case n if n > 0:
        print("Positivo")
    case n if n == 0:
        print("Zero")
