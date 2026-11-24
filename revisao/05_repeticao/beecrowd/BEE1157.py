"""
beecrowd 1157 - Divisores I
https://www.beecrowd.com.br/judge/pt/problems/view/1157
"""

N = int(input())

for i in range(1, N + 1):
    if N % i == 0:
        print(i)
