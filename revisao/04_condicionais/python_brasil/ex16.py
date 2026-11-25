"""
Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
op = input("Operação: (+ - / // % * **): ")

res = 0
match op:
    case "+":
        res = x + y
    case "-":
        res = x - y
    case "*":
        res = x * y
    case "**":
        res = x**y
    case "/":
        if y == 0:
            print("Divisão por zero não é possível calcular")
            res = None
        else:
            res = x / y
    case "//":
        if y == 0:
            print("Divisão por zero não é possível calcular")
            res = None
        else:
            res = x // y
    case "%":
        if y == 0:
            print("Divisão por zero não é possível calcular")
            res = None
        else:
            res = x % y
    case _:
        print("Opção inválida")
        res = None


if res is not None:
    print(f"{x} {op} {y} = {res}")
    print(f"Par ou Ímpar: {'PAR' if res % 2 == 0 else 'ÍMPAR'}")
    print(f"Positivo ou Negativo: {'POSITIVO' if res >= 0 else 'NEGATIVO'}")
    print(f"Inteiro ou Decimal: {'DECIMAL' if float(res) != round(res) else 'INTEIRO'}")
