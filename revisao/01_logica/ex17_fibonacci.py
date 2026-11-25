# Leia N para os N primeiros termos de Fibonnaci
n = int(input("Digite n para exibir n termos da sequência de Fibonacci: "))


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, n + 1):
    print(fibonacci(i), end=" ")
