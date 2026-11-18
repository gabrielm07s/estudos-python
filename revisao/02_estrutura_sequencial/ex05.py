n = int(input('Digite um número: '))

print(f'Centena: {n // 100}')
n %= 100
print(f'Dezena: {n // 10}')
n %= 10
print(f'Unidade: {n}')