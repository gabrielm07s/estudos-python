"""
beecrowd 1013 - O Maior
https://www.beecrowd.com.br/judge/pt/problems/view/1013
"""

A, B, C = map(int, input().split())

MAIOR_AB = (A + B + abs(A - B)) // 2
MAIOR_ABC = (MAIOR_AB + C + abs(MAIOR_AB - C)) // 2

print(f"{MAIOR_ABC} eh o maior")
