"""
beecrowd 1066 - Pares, Ímpares, Positivos e Negativos
https://www.beecrowd.com.br/judge/pt/problems/view/1066
"""

VALORES_PARES = 0
VALORES_IMPARES = 0
VALORES_POSITIVOS = 0
VALORES_NEGATIVO = 0

for i in range(5):
    NUM = int(input())

    if NUM % 2 == 0:
        VALORES_PARES += 1
    else:
        VALORES_IMPARES += 1

    if NUM > 0:
        VALORES_POSITIVOS += 1
    elif NUM < 0:
        VALORES_NEGATIVO += 1

print(f"{VALORES_PARES} valor(es) par(es)")
print(f"{VALORES_IMPARES} valor(es) impar(es)")
print(f"{VALORES_POSITIVOS} valor(es) positivo(s)")
print(f"{VALORES_NEGATIVO} valor(es) negativo(s)")
