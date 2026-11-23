"""
Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turno_estudo = input("Em que turno você estuda: ")

if turno_estudo == "M":
    print("Bom dia!")
elif turno_estudo == "V":
    print("Boa tarde!")
elif turno_estudo == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")
