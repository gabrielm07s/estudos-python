# Somar digitos de um número inteiro lido
num = int(input('Digite um número: '))
valor = num
soma_digitos = 0

while True:
    soma_digitos += valor // 10
    valor %= 10

    if valor // 10 == 0:
        soma_digitos += valor
        break

print(f'A soma dos dígitos do número {num} é {soma_digitos}')