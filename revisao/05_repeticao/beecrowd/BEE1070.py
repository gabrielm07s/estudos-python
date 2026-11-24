"""
beecrowd 1070 - Seis Números Ímpares
https://www.beecrowd.com.br/judge/pt/problems/view/1070
"""

X = int(input())

contador = 0

while contador < 6:
    if X % 2 != 0:
        print(X)
        X += 1
        contador += 1
    else:
        X += 1
