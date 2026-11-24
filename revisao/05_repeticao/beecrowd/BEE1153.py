"""
beecrowd 1153 - Fatorial Simples
https://www.beecrowd.com.br/judge/pt/problems/view/1153
"""

N = int(input())
FAT = 1

for i in range(N, 0, -1):
    FAT *= i

print(FAT)
