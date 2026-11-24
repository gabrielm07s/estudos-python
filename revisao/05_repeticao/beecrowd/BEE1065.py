"""
beecrowd 1065 - Pares entre Cinco Números
https://www.beecrowd.com.br/judge/pt/problems/view/1065
"""

VALORES_PARES = 0

for i in range(5):
    NUM = int(input())

    if NUM % 2 == 0:
        VALORES_PARES += 1

print(f"{VALORES_PARES} valores pares")
