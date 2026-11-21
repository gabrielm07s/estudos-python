# Cacular raízes de uma equação do 2º grau ou mostrar "Impossível calcular"
from math import sqrt

a, b, c = map(float, input().split())
print(f"{int(a)}x² {int(b):+}x {int(c):+}")

delta = b**2 - (4 * a * c)

if delta < 0 or a == 0:
    print("Impossível calcular")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f"Raízes: x' = {x1}, x'' = {x2}")
