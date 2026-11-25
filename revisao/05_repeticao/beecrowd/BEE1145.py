"""
beecrowd 1145 - Sequência Lógica 2
https://www.beecrowd.com.br/judge/pt/problems/view/1145
"""

X, Y = map(int, input().split())

for i in range(1, Y + 1):
    if i % X == 0:
        print(i)
        continue
    print(i, end=" ")
