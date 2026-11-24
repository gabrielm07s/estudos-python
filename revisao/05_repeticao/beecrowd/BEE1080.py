"""
beecrowd 1080 - Maior e Posição
https://www.beecrowd.com.br/judge/pt/problems/view/1080
"""

MAIOR = None
POSICAO_MAIOR = 0

for i in range(1, 101):
    N = int(input())

    if MAIOR is None or N > MAIOR:
        MAIOR = N
        POSICAO_MAIOR = i

print(MAIOR)
print(POSICAO_MAIOR)
