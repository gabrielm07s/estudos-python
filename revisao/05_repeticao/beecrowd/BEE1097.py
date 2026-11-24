"""
beecrowd 1097 - Sequência IJ 3
https://www.beecrowd.com.br/judge/pt/problems/view/1097
"""

I = 1
J = 7
X = 1

while I <= 9:
    print(f"{I=} {J=}")

    if X % 3 == 0:
        I += 2
        J += 4
    else:
        J -= 1

    X += 1
