"""
beecrowd 1176 - Fibonacci em Vetor
https://judge.beecrowd.com/pt/problems/view/1176
"""

FIB = []
T = int(input())

A, B = 0, 1
FIB.extend([A, B])

for i in range(2, 61):
    C = A + B
    A, B = B, C
    FIB.append(C)

for i in range(T):
    X = int(input())

    print(f"Fib({X}) = {FIB[X]}")
