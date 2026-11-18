"""
Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
"""

from math import pi

raio = float(input("Raio do círculo: "))

area = pi * raio**2
print(f"Área do círculo: {area:.2f}")
