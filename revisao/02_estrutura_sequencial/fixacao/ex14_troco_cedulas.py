# Troco em cédulas
valor = float(input('Valor do saque (R$): '))

notas = {
    "200": 200,
    "100": 100,
    "50": 50,
    "20": 20,
    "10": 10,
    "5": 5,
    "2": 2,
}

for nome, cedula in notas.items():
    qtd_notas = int(valor // cedula)
    print(f'Nota de {nome} R$ = {qtd_notas}') 
    valor %= cedula

print(f'Sobraram {round(valor, 2)} R$')