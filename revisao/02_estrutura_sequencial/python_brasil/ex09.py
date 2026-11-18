"""
Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
"""

temperatura_f = float(input("Digite a temperatura em ºF: "))
temperatura_c = ((temperatura_f - 32) * 5) / 9

print(f"{temperatura_f:.1f} ºF = {temperatura_c:.1f} ºC")
