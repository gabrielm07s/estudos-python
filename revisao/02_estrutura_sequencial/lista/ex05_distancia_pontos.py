import math

x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]
print(f'Ponto A: {(x1, y1)}')
print(f'Ponto B: {(x2, y2)}')

d_AB = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f'Distância entre os pontos A e B: {d_AB}')