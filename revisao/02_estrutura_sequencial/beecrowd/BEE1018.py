"""
beecrowd 1018 - Cédulas
https://www.beecrowd.com.br/judge/pt/problems/view/1018
"""

N = int(input())

BAKNOTES = {
    "100,00": 100,
    "50,00": 50,
    "20,00": 20,
    "10,00": 10,
    "5,00": 5,
    "2,00": 2,
    "1,00": 1,
}

print(N)

for NOTE, VALUE in BAKNOTES.items():
    QUANTITY = int(N // VALUE)
    print(f"{QUANTITY} nota(s) de R$ {NOTE}")
    N %= VALUE
