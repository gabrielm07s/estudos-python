"""
beecrowd 1067 - Números Ímpares
https://www.beecrowd.com.br/judge/pt/problems/view/1067
"""

X = int(input())

for i in range(1, X + 1):
    if i % 2 != 0:
        print(i)
