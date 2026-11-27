from math import sqrt

p1 = (1, 2, 3)
p2 = (4, 5, 6)

x1, y1, z1 = p1
x2, y2, z2 = p2

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
print(f"Distância entre {p1} e {p2} é de: {d:.2f}")
