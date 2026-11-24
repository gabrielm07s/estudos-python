"""
beecrowd 1072 - Intervalo 2
https://www.beecrowd.com.br/judge/pt/problems/view/1072
"""

N = int(input())

DENTRO = 0
FORA = 0

for i in range(N):
    X = int(input())

    if 10 <= X <= 20:
        DENTRO += 1
    else:
        FORA += 1

print(f"{DENTRO} in")
print(f"{FORA} out")
