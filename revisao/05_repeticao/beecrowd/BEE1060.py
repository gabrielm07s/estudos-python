"""
beecrowd 1060 - Números Positivos
https://www.beecrowd.com.br/judge/pt/problems/view/1060
"""

VALORES_POSITIVOS = 0

for i in range(6):
    NUM = float(input())

    if NUM > 0:
        VALORES_POSITIVOS += 1

print(f"{VALORES_POSITIVOS} valores positivos")
