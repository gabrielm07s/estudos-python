# Decompor um valor em notas
dinheiro = float(input('Digite um valor: R$ '))
valor = dinheiro

notas = {
    "200": 200,
    "100": 100,
    "50": 50,
    "20": 20,
    "10": 10,
    "5": 5,
    "2": 2
}

moedas = {
    "100": 100,
    "75": 75,
    "50": 50,
    "25": 25,
    "10": 10,
    "5": 5
}

print(f'VALOR: {valor:.2f}')

print('\nNOTAS:')
for nome, cedula in notas.items():
    qtd = int(valor // cedula)
    print(f'Notas de {nome}: {qtd}')
    valor %= cedula

print('\nMOEDAS:')
valor *= 100
for nome, moeda in moedas.items():
    qtd = int(valor // moeda)
    print(f'Moedas de {nome}: {qtd}')
    valor %= moeda