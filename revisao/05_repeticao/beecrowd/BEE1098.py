"""
beecrowd 1098 - Sequência IJ 4
https://www.beecrowd.com.br/judge/pt/problems/view/1098
"""

I = 0
J = 1
X = 1

while I <= 2:
    print(f"I={I:g} J={J:g}")

    if X % 3 == 0:
        I = round(I + 0.2, 1)
        J = round(J - 1.8, 1)
    else:
        J += 1

    X += 1
