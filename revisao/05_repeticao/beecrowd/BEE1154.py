"""
beecrowd 1154 - Idades
https://www.beecrowd.com.br/judge/pt/problems/view/1154
"""

TOTAL_IDADES = 0
SOMA_IDADES = 0

while True:
    IDADE = int(input())

    if IDADE < 0:
        break

    SOMA_IDADES += IDADE
    TOTAL_IDADES += 1

IDADE_MEDIA = SOMA_IDADES / TOTAL_IDADES
print(f"{IDADE_MEDIA:.2f}")
