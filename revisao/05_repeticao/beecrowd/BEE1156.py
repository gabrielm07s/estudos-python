"""
beecrowd 1156 - Sequência S II
https://www.beecrowd.com.br/judge/pt/problems/view/1156
"""

S = 0
NUMERADOR, DENOMINADOR = 1, 1

while NUMERADOR <= 39:
    S += NUMERADOR / DENOMINADOR

    NUMERADOR += 2
    DENOMINADOR *= 2

print(f"{S:.2f}")
