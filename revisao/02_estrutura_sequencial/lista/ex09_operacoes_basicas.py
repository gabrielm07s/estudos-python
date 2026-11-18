# Leia dois números e msotre a soma, subtração, produto, divisão, divisão inteira, resto e potência
n1, n2 = [float(x) for x in input().split()]

print(f'Soma: {n1 + n2}')
print(f'Subtração: {n1 - n2}')
print(f'Produto: {n1 * n2}')

if n2 == 0:
    print('Não existe divisão por zero!')
    print('Não foi possível calcular a divisão, divisão inteira e o resto')
else:
    print(f'Divisão: {n1 / n2}')
    print(f'Divisão Inteira: {n1 // n2}')
    print(f'Resto: {n1 % n2}')
print(f'Potência: {n1 ** n2}')