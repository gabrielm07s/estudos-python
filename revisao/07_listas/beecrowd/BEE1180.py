"""
beecrowd 1180 - Menor e Posição
https://judge.beecrowd.com/pt/problems/view/1180
"""

N = int(input())
X = []

valores = map(int, input().split())
X.extend(valores)

print(f"Menor valor: {min(X)}")
print(f"Posicao: {X.index(min(X))}")
