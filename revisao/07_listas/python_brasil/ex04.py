"""
Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vetor = []

for i in range(10):
    c = input(f"Digite o {i + 1}º caractere: ")
    vetor.append(c)

consoantes = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
]

consoantes_digitadas = [x for x in vetor if x in consoantes]
print(f"Foram digitadas {len(consoantes_digitadas)} consoantes, sendo elas:")
print(consoantes_digitadas)
