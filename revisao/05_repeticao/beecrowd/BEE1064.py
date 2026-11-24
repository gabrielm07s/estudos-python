"""
beecrowd 1064 - Positivos e Média
https://www.beecrowd.com.br/judge/pt/problems/view/1064
"""

VALORES_POSITIVOS = 0
SOMA_POSITIVOS = 0

for i in range(6):
    NUM = float(input())

    if NUM > 0:
        VALORES_POSITIVOS += 1
        SOMA_POSITIVOS += NUM

print(f"{VALORES_POSITIVOS} valores positivos")

MEDIA_POSITIVOS = SOMA_POSITIVOS / VALORES_POSITIVOS
print(f"{MEDIA_POSITIVOS:.1f}")
