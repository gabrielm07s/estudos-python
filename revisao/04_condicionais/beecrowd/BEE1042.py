"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Exemplo de Entrada	Exemplo de Saída
7 21 -14

-14
7
21

7
21
-14

-14 21 7

-14
7
21

-14
21
7
"""

A, B, C = map(int, input().split())

NUMEROS_ORDENADO = [A, B, C]
NUMEROS_ORDENADO.sort()

for N in NUMEROS_ORDENADO:
    print(N)

print()

for N in (A, B, C):
    print(N)
