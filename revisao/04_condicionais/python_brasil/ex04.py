"""
Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input("Digite uma letra: ").strip().lower()

vogais = ["a", "e", "i", "o", "u"]
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

if letra in vogais:
    print("Vogal")
elif letra in consoantes:
    print("Consoante")
else:
    print("Não é uma letra")
