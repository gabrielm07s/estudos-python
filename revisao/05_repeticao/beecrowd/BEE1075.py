"""
beecrowd 1075 - Resto 2
https://www.beecrowd.com.br/judge/pt/problems/view/1075
"""

N = int(input())

for i in range(1, 10001):
    if i % N == 2:
        print(i)
