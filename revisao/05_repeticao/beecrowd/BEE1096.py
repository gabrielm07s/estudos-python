"""
beecrowd 1096 - Sequência IJ 2
https://www.beecrowd.com.br/judge/pt/problems/view/1096
"""

I = 1
J = 7
X = 1

while I <= 9:
    print(f"{I=} {J=}")

    if X % 3 == 0:
        I += 2
        J += 2
    else:
        J -= 1

    X += 1
