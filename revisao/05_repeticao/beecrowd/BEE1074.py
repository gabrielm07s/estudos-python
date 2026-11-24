"""
beecrowd 1074 - Par ou Ímpar
https://www.beecrowd.com.br/judge/pt/problems/view/1074
"""

N = int(input())

for i in range(N):
    X = int(input())

    if X == 0:
        print("NULL")
        continue

    PARITY = "EVEN" if X % 2 == 0 else "ODD"
    SIGNAL = "POSITIVE" if X > 0 else "NEGATIVE"

    print(PARITY, SIGNAL)
