"""
Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

temperatura_c = float(input("Digite a temperatura em ºC: "))
temperatura_f = (temperatura_c * 1.8) + 32

print(f"{temperatura_c:.1f} ºC = {temperatura_f:.1f} ºF")
