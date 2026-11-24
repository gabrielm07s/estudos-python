"""
beecrowd 1155 - Sequência S
https://www.beecrowd.com.br/judge/pt/problems/view/1155
"""

S = 0

for i in range(1, 101):
    S += 1 / i

print(f"{S:.2f}")
