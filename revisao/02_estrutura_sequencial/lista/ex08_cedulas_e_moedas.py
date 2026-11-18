valor = float(input())

cedulas = {
    "200": 200,
    "100": 100,
    "50": 50,
    "20": 20,
    "10": 10,
    "5": 5,
    "2": 2
}

centavos = {
    "100": 100,
    "50": 50,
    "25": 25,
    "10": 10,
    "5": 5,
    "1": 1,
}

print('\nNOTAS: ')
for nome, cedula in cedulas.items():
    qtd_cedula = int(valor // cedula)
    print(f'Quantidade de notas de {nome} R$ == {qtd_cedula}')
    valor %= cedula

valor = round(valor * 100, 2)
print('\nMOEDAS:')
for nome, centavo in centavos.items():
    qtd_centavos = int(valor // centavo)
    print(f'Quantidade de moedas de {nome} centavos == {qtd_centavos}')
    valor %= centavo