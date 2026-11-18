valor = int(input())

cedulas = {
    "200": 200,
    "100": 100,
    "50": 50,
    "20": 20,
    "10": 10,
    "5": 5,
    "2": 2
}

for nome, cedula in cedulas.items():
    qtd_cedula = int(valor // cedula)
    print(f'Quantidade de notas de {nome} R$ == {qtd_cedula}')
    valor %= cedula