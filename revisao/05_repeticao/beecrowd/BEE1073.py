"""
beecrowd 1073 - Quadrado de Pares
https://www.beecrowd.com.br/judge/pt/problems/view/1073
"""

N = int(input())

for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i}^{2} = {i**2}")
