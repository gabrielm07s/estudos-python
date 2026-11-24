"""
beecrowd 1079 - Médias Ponderadas
https://www.beecrowd.com.br/judge/pt/problems/view/1079
"""

N = int(input())

for i in range(N):
    N1, N2, N3 = map(float, input().split())

    MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 5)) / 10.0
    print(f"{MEDIA:.1f}")
