"""
beecrowd 1116 - Dividindo X por Y
https://www.beecrowd.com.br/judge/pt/problems/view/1116
"""

N = int(input())

for i in range(N):
    X, Y = map(int, input().split())

    if Y == 0:
        print("divisao impossivel")
    else:
        print(f"{X / Y:.1f}")
