n1, n2 = map(float, input("n1, n2: ").split())
operador = input("(+, -, /, //, *, **, %): ")

res = None
match operador:
    case "+":
        res = n1 + n2
    case "-":
        res = n1 - n2
    case "*":
        res = n1 * n2
    case "**":
        res = n1**n2
    case "/":
        if n2 == 0:
            print("Divisão por zero não é permitida")
        else:
            res = n1 / n2
    case "//":
        if n2 == 0:
            print("Divisão por zero não é permitida")
        else:
            res = n1 // n2
    case "%":
        if n2 == 0:
            print("Divisão por zero não é permitida")
        else:
            res = n1 % n2
    case _:
        print("Operação inválida")

print(f"Resultado: {n1} {operador} {n2} = {res}")
