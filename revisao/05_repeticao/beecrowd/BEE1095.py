"""
beecrowd 1095 - Sequência IJ 1
https://www.beecrowd.com.br/judge/pt/problems/view/1095
"""

I = 1
J = 60
X = 2

while J >= 0:
    print(f"{I=} {J=}")

    I = (3 * X) - 2
    J = (-5 * X) + 65
    X += 1
