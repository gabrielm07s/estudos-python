num_func, horas = [int(x) for x in input().split()]
valor_hora = float(input())

salario = horas * valor_hora
print(f'[{num_func}] - R$ {salario:.2f}')