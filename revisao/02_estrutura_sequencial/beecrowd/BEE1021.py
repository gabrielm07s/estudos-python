"""
beecrowd 1021 - Notas e Moedas
https://www.beecrowd.com.br/judge/pt/problems/view/1021
"""

N = float(input())

BAKNOTES = {
    "100.00": 100,
    "50.00": 50,
    "20.00": 20,
    "10.00": 10,
    "5.00": 5,
    "2.00": 2,
}

COINS = {
    "1.00": 100,
    "0.50": 50,
    "0.25": 25,
    "0.10": 10,
    "0.05": 5,
    "0.01": 1,
}


def COUNT_NOTES(DICT, NOME):
    global N
    for NAME, VALUE in DICT.items():
        QUANTITY = int(N // VALUE)
        print(f"{QUANTITY} {NOME}(s) de R$ {NAME}")
        N %= VALUE


print("NOTAS:")
COUNT_NOTES(BAKNOTES, "nota")

N = round(N * 100, 2)
print("MOEDAS:")
COUNT_NOTES(COINS, "moeda")
