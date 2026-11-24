"""
beecrowd 1101 - Sequência de Números e Soma
https://www.beecrowd.com.br/judge/pt/problems/view/1101
"""

while True:
    M, N = map(int, input().split())

    if M <= 0 or N <= 0:
        break

    MAIOR, MENOR = max(M, N), min(M, N)

    for i in range(MENOR, MAIOR + 1):
        print(i, end=" ")

    print(f"Sum={sum([x for x in range(MENOR, MAIOR + 1)])}")
