"""
beecrowd 1151 - Fibonacci Fácil
https://www.beecrowd.com.br/judge/pt/problems/view/1151
"""

N = int(input())
A, B = 0, 1

for i in range(N):
    print(A, end="\n" if i == N - 1 else " ")
    A, B = B, A + B
