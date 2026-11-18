# Leia um valor em metros e mostre em centímetros, milímetros, quilômetros
valor = float(input())

print(f'{valor} m')
print(f'{valor * 100} cm')
print(f'{valor * 1000} mm')
print(f'{valor / 1000} km')