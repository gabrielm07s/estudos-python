"""
beecrowd 1144 - Sequência Lógica
https://www.beecrowd.com.br/judge/pt/problems/view/1144
"""

N = int(input())
X, Y, Z = 1, 1, 1

for i in range(N):
    print(X, Y, Z)
    print(X, Y + 1, Z + 1)
    X += 1
    Y = X**2
    Z = X**3
